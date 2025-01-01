"""
对原版mcfunction语句的封装
"""

from .core import MCF
from typing import Any, Literal, TypeAlias, Self, NewType, Callable, Generic

NumericVariableTypes: TypeAlias = Literal[
    'int', 'float', 'short', 'long', 'double', 'byte'
]
IntegerVariableTypes: TypeAlias = Literal[
    'int', 'short', 'long', 'byte'
]
FloatingPointVariableTypes: TypeAlias = Literal[
    'float', 'double'
]

__all__ = [
    'ScoreBoard',
    'Execute',
    'Data',
    'Function',
    'ReturN',
    'Say',
    'Tag',
    'IntegerVariableTypes',
    'NumericVariableTypes',
    'FloatingPointVariableTypes'
]

class _Collector:
    _buffer: str
    def __init__(self):
        pass
    def write(self, s: str) -> int:
        self._buffer = s
        return 1

Execute = NewType("Execute", None)

_ExecuteStoreContext = NewType("_ExecuteStoreContext", None)

class _ExecuteStoreContext:
    _source: Execute
    _built: str

    def __init__(self, src: Execute, built: str):
        self._source = src
        self._built = built

    def block(
        self,
        position: tuple[str, str, str],
        nbt_path: str,
        store_type: NumericVariableTypes,
        scale: float
    ) -> Execute:
        """指定store的目标为block，等价于`... block <position> <nbt_path>
         <store_type> <scale>`
        """
        contents = [
            self._built, 'block', f"{position[0]} {position[1]} {position[2]}",
            nbt_path, store_type, str(scale)
        ]
        self._source._context_feedback(' '.join(contents))
        return self._source

    def storage(
        self,
        storage_name: str,
        nbt_path: str,
        store_type: NumericVariableTypes,
        scale: float
    ) -> Execute:
        """指定store的目标为storage，等价于`... storage <storage_name> <nbt_path>
         <store_type> <scale>`
        """
        contents = [
            self._built, 'storage', storage_name, nbt_path, store_type, str(scale)
        ]
        self._source._context_feedback(' '.join(contents))
        return self._source

    def entity(
        self,
        compiled_selector: str,
        nbt_path: str,
        store_type: NumericVariableTypes,
        scale: float
    ) -> Execute:
        """指定store的目标为entity，等价于`... entity <compiled_selector> <nbt_path>
         <store_type> <scale>`
        """
        contents = [
            self._built, 'entity', compiled_selector, nbt_path, store_type, str(scale)
        ]
        self._source._context_feedback(' '.join(contents))
        return self._source

    def score(
        self,
        score_holder: str,
        board_name: str
    ) -> Execute:
        """指定store的目标为score，等价于`... score <score_holder> <board_name>`"""
        contents = [self._built, 'score', score_holder, board_name]
        self._source._context_feedback(' '.join(contents))
        return self._source

    def bossbar(
        self,
        bossbar_id: str,
        value_type: Literal['max', 'value']
    ) -> Execute:
        """指定store的目标为bossbar，等价于`... bossbar <bossbar_id> <value_type>`"""
        contents = [self._built, 'bossbar', bossbar_id, value_type]
        self._source._context_feedback(' '.join(contents))
        return self._source

_ExecuteConditionContext = NewType("_ExecuteConditionContext", None)

class _ExecuteConditionContext:
    _source: Execute
    _built: str

    def __init__(self, src: Execute, built: str):
        self._source = src
        self._built = built

    def score_matches(
        self,
        score_holder: str,
        board_name: str,
        left: int | None,
        right: int | None
    ) -> Execute:
        """以matches模式判断分数范围，
        等价于`... score <score_holder> <board_name> matches <left>..<right>`
        """
        if left is None and right is None: return self._source
        ls = '' if left is None else str(left)
        rs = '' if right is None else str(right)
        range_str = str()
        if ls != rs:
            range_str = f"{ls}..{rs}"
        else:
            range_str = ls
        contents = [
            self._built, 'score', score_holder, board_name,
            'matches', range_str
        ]
        self._source._context_feedback(' '.join(contents))
        return self._source

    def score_compare(
        self,
        score_holder_left: str,
        board_name_left: str,
        compare: str,
        score_holder_right: str,
        board_name_right: str
    ) -> Execute:
        """以compare模式比较分数大小，
        等价于`... score <score_holder_left> <board_name_left>
         <compare> <score_holder_right> <board_name_right>`
        """
        contents = [
            self._built, 'score', score_holder_left, board_name_left,
            compare, score_holder_right, board_name_right
        ]
        self._source._context_feedback(' '.join(contents))
        return self._source

class Execute:
    """execute系列命令的封装"""

    sub_commands: list[str]
    is_macro: bool
    collect: _Collector
    _last_redirect: Any

    def __init__(self, macro: bool = False):
        self.sub_commands = ["execute"]
        self.is_macro = macro
        self.collect = _Collector()
        self._last_redirect = MCF._io_redirect
        MCF.redirect(self.collect)

    def condition(self, mode: Literal['if', 'unless']) -> _ExecuteConditionContext:
        """创建一个条件子命令，等价于`(if|unless) ...`"""
        return _ExecuteConditionContext(self, mode)

    def store(self, mode: Literal['result', 'success']) -> _ExecuteStoreContext:
        """创建一个储存子命令，等价于`store (result|success) ...`"""
        return _ExecuteStoreContext(self, f"store {mode}")

    def aS(self, compiled_selector: str) -> Execute:
        self.sub_commands.append(
            f"as {compiled_selector}"
        )
        return self

    def _context_feedback(self, sub_command: str) -> None:
        self.sub_commands.append(sub_command)

    def run(self, run_command: None) -> None:
        """执行子命令，在括号中调用命令，接收其返回值作为参数（返回值始终为`None`）"""
        self.sub_commands.append('run')
        self.sub_commands.append(self.collect._buffer.removeprefix('$'))
        MCF.redirect(self._last_redirect)
        MCF.write(' '.join(self.sub_commands), self.is_macro)

class ScoreBoard:
    """所有与scoreboard相关的指令封装"""
    def __init__(self):
        pass
    
    @staticmethod
    def players_set(
        score_holder: str,
        board_name: str,
        value: int | str,
        macro: bool = False
    ) -> None:
        """等同于`scoreboard players set <score_holder> <board_name>
          <value>`
        """
        MCF.write(
f"""scoreboard players set {score_holder} {board_name} {value}
"""
        , macro)

    @staticmethod
    def players_operation(
        score_holder_to: str,
        board_name_to: str,
        operation: str,
        score_holder_from: str,
        board_name_from: str,
        macro: bool = False
    ) -> None:
        """等同于`scoreboard players operation <score_holder_to>
          <board_name_to> <operation> <score_holder_from> <board_name_from>`
        """
        MCF.write(
f"""scoreboard players operation {score_holder_to} {board_name_to} {operation} {score_holder_from} {board_name_from}
"""
        , macro)

    @staticmethod
    def players_add(
        score_holder: str,
        board_name: str,
        value: int | str,
        macro: bool = False
    ) -> None:
        """等同于`scoreboard players add <score_holder> <board_name> <value>`"""
        MCF.write(
f"""scoreboard players add {score_holder} {board_name} {value}
"""
        , macro)

    @staticmethod
    def players_reset(
        score_holder: str,
        board_name: str,
        macro: bool = False
    ) -> None:
        """等同于`scoreboard players reset <score_holder> <board_name>`"""
        MCF.write(
f"""scoreboard players reset {score_holder} {board_name}
"""
        , macro)

    @staticmethod
    def players_remove(
        score_holder: str,
        board_name: str,
        value: int | str,
        macro: bool = False
    ) -> None:
        MCF.write(
f"""scoreboard players remove {score_holder} {board_name} {value}
"""
        , macro)

    @staticmethod
    def players_get(
        score_holder: str,
        board_name: str,
        macro: bool = False
    ) -> None:
        """等同于`scoreboard players get <score_holder> <board_name>`"""
        MCF.write(
f"""scoreboard players get {score_holder} {board_name}
"""
        , macro)

    @staticmethod
    def to_storage(
        dist: str,
        score_holder: str,
        board_name: str,
        scale: float,
        _type: NumericVariableTypes = 'int',
        macro: bool = False
    ) -> None:
        """将位于`<score_holder> <board_name>`位置的计分板数据移动至项目储存
        的`<dist>`路径内，并乘上`<scale>`。
        """
        MCF.write(
f"""execute store result storage {MCF.storage} {dist} {_type} {scale} run scoreboard players get {score_holder} {board_name}
"""
        , macro)
    
    @staticmethod
    def from_storage(
        src: str,
        score_holder: str,
        board_name: str,
        scale: float,
        macro: bool = False
    ) -> None:
        """将位于项目储存的`<src>`路径位置的数据移动至计分板的
        的`<score_holder> <board_name>`位置，并乘上`<scale>`。
        """
        MCF.write(
f"""execute store result score {score_holder} {board_name} run data get storage {MCF.storage} {src} {scale}
"""
        , macro)

_DataModification = NewType("_DataModification", None)

class _DataTarget:
    _target: str
    def __init__(self, target: str):
        self._target = target

    def get(
        self,
        nbt_path: str| None = None,
        scale: float| None = None,
        macro: bool = False
    ) -> None:
        """对指定的操作对象做get操作，等价于`data get (target)
        [nbt_path] [scale]`
        """
        contents = ['data get', self._target]
        if nbt_path is not None:
            contents.append(nbt_path)
        if scale is not None:
            contents.append(str(scale))
        MCF.write(' '.join(contents) + '\n', macro)

    def merge(
        self,
        compiled_snbt: str,
        macro: bool = False
    ) -> None:
        """对指定的操作对象做merge操作，等价于`data merge (target)
        <compiled_snbt>`
        """
        MCF.write(
            ' '.join(['data merge', self._target, compiled_snbt]) + '\n',
            macro
        )

    def remove(
        self,
        nbt_path: str,
        macro: bool = False
    ) -> None:
        """对指定的操作对象做remove操作，等价于`data remove (target) <nbt_path>`"""
        MCF.write(
            ' '.join(['data remove', self._target, nbt_path]) + '\n',
            macro
        )

    def modify_append(
        self,
        nbt_path: str,
        macro: bool = False
    ) -> _DataModification:
        """对指定操作目标做modify操作，具体模式为append，等价于
        `data modify (target) <nbt_path> append ...`
        """
        return _DataModification(
            ' '.join(['data modify', self._target, f'{nbt_path} append']), macro
        )

    def modify_insert(
        self,
        nbt_path: str,
        index: int,
        macro: bool = False
    ) -> _DataModification:
        """对指定操作目标做modify操作，具体模式为insert，等价于
        `data modify (target) <nbt_path> insert <index> ...`
        """
        return _DataModification(
            ' '.join(['data modify', self._target, f'{nbt_path} insert {index}']),
            macro
        )

    def modify_merge(
        self,
        nbt_path: str,
        macro: bool = False
    ) -> _DataModification:
        """对指定操作目标做modify操作，具体模式为merge，等价于
        `data modify (target) <nbt_path> merge ...`
        """
        return _DataModification(
            ' '.join(['data modify', self._target, f'{nbt_path} merge']), macro
        )

    def modify_prepend(
        self,
        nbt_path: str,
        macro: bool = False
    ) -> _DataModification:
        """对指定操作目标做modify操作，具体模式为prepend，等价于
        `data modify (target) <nbt_path> prepend ...`
        """
        return _DataModification(
            ' '.join(['data modify', self._target, f'{nbt_path} prepend']), macro
        )

    def modify_set(self,
        nbt_path: str,
        macro: bool = False
    ) -> _DataModification:
        """对指定操作目标做modify操作，具体模式为set，等价于
        `data modify (target) <nbt_path> set ...`
        """
        return _DataModification(
            ' '.join(['data modify', self._target, f'{nbt_path} set']), macro
        )

class _DataModification:
    _built: str
    _macro: bool
    def __init__(self, built: str, macro: bool):
        self._built = built
        self._macro = macro

    def via(
        self, 
        target: _DataTarget,
        nbt_path: str | None = None
    ) -> None:
        """指定modify的方式为from，等价于
        `data modify ... from (target) [nbt_path]`
        """
        contents = [self._built, 'from', target._target]
        if nbt_path is not None: contents.append(nbt_path)
        MCF.write(' '.join(contents) + '\n', self._macro)

    def string(
        self,
        target: _DataTarget,
        nbt_path: str | None = None,
        start: int | None = None,
        end: int | None = None
    ) -> None:
        """指定modify的方式为string，等价于
        `data modify ... string (target) [nbt_path] [start] [end]`
        """
        contents = [self._built, 'string', target._target]
        if nbt_path is not None: contents.append(nbt_path)
        if start is not None: contents.append(start)
        if end is not None: contents.append(end)
        MCF.write(' '.join(contents) + '\n', self._macro)

    def value(self, value: str) -> None:
        """指定modify的方式为value，等价于`data modify ... value <value>`"""
        MCF.write(' '.join([self._built, 'value', value]) + '\n', self._macro)

class Data:
    """data系列命令的封装"""    

    @staticmethod
    def block(
        x: int | str,
        y: int | str,
        z: int | str
    ) -> _DataTarget:
        """创建data命令的操作对象为`block <x> <y> <z>`"""
        return _DataTarget(f"block {x} {y} {z}")
    
    @staticmethod
    def entity(compiled_selector: str) -> _DataTarget:
        """创建data命令的操作对象为`entity <compiled_selector>`"""
        return _DataTarget(f"entity {compiled_selector}")
    
    @staticmethod
    def storage(storage_name: str) -> _DataTarget:
        """创建data命令的操作对象为`storage <storage_name>`"""
        return _DataTarget(f"storage {storage_name}")
    
class Function:
    """function命令的封装"""
    _signature: str
    _macro: bool
    def __init__(self, signature: str, macro: bool = False):
        self._signature = signature
        self._macro = macro
    
    def call(self, compiled_snbt: str | None = None) -> None:
        """使用函数，等价于`function <signature> [compiled_snbt]`"""
        contents = ['function', self._signature]
        if compiled_snbt is not None: contents.append(compiled_snbt)
        MCF.write(' '.join(contents) + '\n', self._macro)

    def with_args(
        self,
        target: _DataTarget,
        nbt_path: str | None = None
    ) -> None:
        """使用函数，等价于`function <signature> with (target) [nbt_path]`"""
        contents = ['function', self._signature, 'with', target._target]
        if nbt_path is not None: contents.append(nbt_path)
        MCF.write(' '.join(contents) + '\n', self._macro)

class ReturN:
    """return命令的封装"""
    _macro: bool
    _collect: _Collector
    _last_redirect: Any
    def __init__(self, macro: bool = False):
        self._macro = macro
        self._collect = _Collector()
        self._last_redirect = MCF._io_redirect
        MCF.redirect(self._collect)
    
    def value(self, value: int | str) -> None:
        """返回值，等价于`return <value>`"""
        MCF.redirect(self._last_redirect)
        MCF.write(f'return {value}\n', self._macro)
        

    def run(self, run_command: None) -> None:
        """执行返回前命令，在括号中调用命令，
        接收其返回值作为参数（返回值始终为`None`）
        """
        MCF.redirect(self._last_redirect)
        MCF.write(
            'return run ' + self._collect._buffer.removeprefix('$'),
            self._macro
        )

def Say(content: str, macro: bool = False) -> None:
    MCF.write(
        f"say {content}\n", macro
    )

class Tag:
    _select: str
    _macro: bool
    def __init__(self, compiled_selector: str, macro: bool = False):
        self._select = compiled_selector
        self._macro = macro
    
    def add(self, tag: str) -> None:
        MCF.write(
            f"tag {self._select} add {tag}\n", self._macro
        )
    
    def list(self) -> None:
        MCF.write(
            f"tag {self._select} list\n", self._macro
        )
    
    def remove(self, tag: str) -> None:
        MCF.write(
            f"tag {self._select} remove {tag}\n", self._macro
        )

