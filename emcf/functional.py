
from .core import MCF
from ._exceptions import MCFTypeError, MCFSyntaxError
from .types import *
from ._writers import *
from ._writers import _MultiCollector
from ._utils import console
from typing import (
    Callable, TypeVar, TypeVarTuple, Generic,
    Type, Any, get_origin, TypeAlias, Annotated
)
from functools import wraps

__all__ = [
    'Ref',
    'ConditionRef',
    'IntegerRef',
    'FloatRef',
    'MCFunction',
    'Return'
]

class Ref:
    _wrapped: Any
    def __init__(self, value: Any):
        super().__init__()
        if not isinstance(value, MCFVariable):
            console.error(
                MCFTypeError(
                    "Can not use Ref on type: {}",
                    type(value)
                )
            )
        self._wrapped = value

ConditionRef: TypeAlias = Annotated[Condition, Ref]
IntegerRef: TypeAlias = Annotated[Integer, Ref]
FloatRef: TypeAlias = Annotated[Float, Ref]

# default argument value is not supported at present

def push_stack() -> None:
    index = 0
    for var in MCF._context.values():
        var.move(f"frame.m{index}")
        index += 1
    # 保存栈帧
    Data.storage(MCF.storage).modify_set("frame.cond_stack").via(
        Data.storage(MCF.storage), "cond_stack"
    )
    Execute().store('result').storage(
        MCF.storage, "frame.terminate", 'byte', 1.0
    ).run(
        ScoreBoard.players_get(MCF.TERMINATE, MCF.sb_sys)
    )
    Data.storage(MCF.storage).modify_set("frame.loop_stack").via(
        Data.storage(MCF.storage), "loop_stack"
    )
    Data.storage(MCF.storage).modify_append("stack").via(
        Data.storage(MCF.storage), "frame"
    )
    Data.storage(MCF.storage).modify_set("frame").value(r"{}")
    MCF._context_stack.append(MCF._context.copy())
    MCF._context.clear()

def new_stack() -> None:
    # 于此添加更多的栈帧默认值
    Data.storage(MCF.storage).modify_set("cond_stack").value("[]")
    Data.storage(MCF.storage).modify_set("loop_stack").value("[]")
    ScoreBoard.players_set(MCF.TERMINATE, MCF.sb_sys, 0)

def pop_stack() -> None:
    MCF._context = MCF._context_stack.pop()
    Data.storage(MCF.storage).modify_set("frame").via(
        Data.storage(MCF.storage), "stack[-1]"
    )
    Data.storage(MCF.storage).remove("stack[-1]")
    # 恢复更多信号寄存器
    Data.storage(MCF.storage).modify_set("cond_stack").via(
        Data.storage(MCF.storage), "frame.cond_stack"
    )
    Execute().store('result').score(MCF.TERMINATE, MCF.sb_sys).run(
        Data.storage(MCF.storage).get("frame.terminate", 1.0)
    )
    Data.storage(MCF.storage).modify_set("loop_stack").via(
        Data.storage(MCF.storage), "frame.loop_stack"
    )
    index = 0
    for var in MCF._context.values():
        var.collect(f"frame.m{index}")
        index += 1

Ret = TypeVar('ReturnValue')
Args = TypeVarTuple('Args')
class MCFunction(Generic[Ret]):
    _entry_path: str
    _entry_sig: str
    _body_path: str
    _body_sig: str
    _exported: bool
    _ret_addr: str | None
    _ret_type: Type[Ret]
    _input_addr: list[str]
    _context: dict[str, MCFVariable]
    _ref_args: dict[str, MCFVariable]
    _collected: list[MCFVariable]

    def __init__(self, ret_type: Type[Ret] = FakeNone):
        self._entry_path, self._entry_sig = MCF.makeFunction()
        self._body_path, self._body_sig = MCF.makeFunction()
        self._ret_addr = MCF.getFID()
        self._exported = False
        self._ret_type = ret_type
        self._input_addr = []
        self._context = {}
        self._ref_args = {}
        self._collected = []

    def _collect_params(self, args: tuple[object]) -> tuple[MCFVariable]:
        collected = []
        index = 0
        for arg in args:
            if isinstance(arg, Ref):
                arg: MCFVariable = arg._wrapped
                new: MCFVariable = arg.macro_construct(
                    f"m{index}", self._input_addr[index]
                )
                collected.append(new)
                index += 1
                self._ref_args[new._mcf_id] = arg
            elif isinstance(arg, MCFVariable):
                new: MCFVariable = arg.macro_construct(
                    f"m{index}", self._input_addr[index]
                )
                collected.append(new)
                index += 1
            else:
                console.error(
                    MCFTypeError(
                        "Parameter '{}' can not be passed to a MCFunction.", arg
                    )
                )
                return args
        return tuple(collected)

    def _export_params(self, args: tuple[object]) -> bool:
        index = 0
        for arg in args:
            if isinstance(arg, Ref):
                arg = arg._wrapped
            if isinstance(arg, MCFVariable):
                Data.storage(MCF.storage).modify_set(
                    f"call.m{index}"
                ).value(
                    f'"{arg._mcf_id}"'
                )
                index += 1
            else:
                console.error(
                    MCFTypeError(
                        "Parameter '{}' can not be passed to a MCFunction.", arg
                    )
                )
                return False
        return True

    def _push_stack(self) -> None:
        push_stack()

    def _new_stack(self) -> None:
        MCF._context.update(self._context)
        new_stack()

    def _pop_stack(self) -> None:
        pop_stack()

    def __call__(self, func: Callable[[*Args], None]) -> Callable[[*Args], Ret]:

        def early_exit():
            if self._ret_type is FakeNone:
                return None
            result = self._ret_type(init_val=None, void=False)
            MCF.addContext(result)
            return result

        @wraps(func)
        def wrapper(*args: *Args) -> Ret:
            # type check
            check_pass = True
            size_args = len(args)
            size_need = len(func.__annotations__)
            if size_args != size_need:
                console.error(
                    MCFSyntaxError(
                        f"Function {func.__name__} needs {size_need} arguments, "
                        f"while {size_args} is provided."
                    )
                )
                return early_exit()
            
            index = 0
            for name, tp in func.__annotations__.items():
                checking = args[index]
                if type(tp) is not type:
                    if (
                        get_origin(tp) is not Annotated
                        or tp.__metadata__[0] is not Ref
                    ):
                        console.error(
                            MCFTypeError(
                                "Invalid type annotation given: {}",
                                tp
                            )
                        )
                        check_pass = False
                        continue
                    tp = tp.__origin__
                    if not isinstance(checking, Ref):
                        console.error(
                            MCFTypeError(
                                f"Argument at position {index + 1} require a Ref"
                                " variable, while a variable of type {} is given.",
                                type(checking)
                            )
                        )
                        check_pass = False
                        continue
                    checking = checking._wrapped
                    
                if not isinstance(checking, tp):
                    console.error(
                        MCFTypeError(
                            f"Given argument {name} at position {index + 1} "
                            "is not an instance of {}.", tp
                        )
                    )
                    check_pass = False
                index += 1
            if not check_pass:
                return early_exit()

            # 为每个参数生成一个Fool ID
            if not self._exported:
                for _ in range(len(args)):
                    self._input_addr.append(MCF.getFID())

            # 将当前上下文压入栈中
            self._push_stack()

            # 将参数导出到存储中
            valid = self._export_params(args)
            if not valid:
                console.error(
                    MCFTypeError(
                        "Failed to call function '{}' for it can not be converted to a MCFunction.",
                        func.__name__
                    )
                )

            # 如果函数未导出，则导出函数
            if not self._exported and valid:
                self._exported = True
                MCF.forward(self._entry_path)
                collected = self._collect_params(args)

                # 储存为函数上下文
                for var in collected:
                    var._gc_sign = 'shadow'
                    self._context[var._mcf_id] = var
                
                # 更新当前上下文
                self._new_stack()
                Function(self._body_sig).call()

                MCF.forward(self._body_path)
                func(*collected)
                MCF.rewind()

                # update collected & gc
                for var in collected:
                    src = self._ref_args.get(var._mcf_id, None)
                    if src is not None:
                        self._collected.append(var)
                    else:
                        if MCF.do_gc:
                            var.rm()

                MCF.rewind()
            else:
                # 更新当前上下文
                self._new_stack()

            Function(self._entry_sig).with_args(
                Data.storage(MCF.storage), "call"
            )

            ret_val = self._ret_type(init_val=None, void=False)
            if isinstance(ret_val, FakeNone):
                ret_val = None
                self._pop_stack()       # 恢复上下文
            else:
                ret_val.collect("ret_val")
                self._pop_stack()           # 恢复上下文
                MCF.addContext(ret_val)     # 将返回值添加至当前上下文
            
            # update ref
            for var in self._collected:
                src = self._ref_args[var._mcf_id]
                src.assign(var)
                if MCF.do_gc:
                    var.rm()

            return ret_val
        
        wrapper.__mcfsignature__ = self._entry_sig
        return wrapper

def Return(ret_value: MCFVariable = FakeNone()) -> None:
    if isinstance(ret_value, FakeNone):
        ScoreBoard.players_set(MCF.TERMINATE, MCF.sb_sys, 1)
    elif isinstance(ret_value, MCFVariable):
        ScoreBoard.players_set(MCF.TERMINATE, MCF.sb_sys, 1)
        ret_value.move("ret_val")
    else:
        console.error(
            MCFTypeError(
                "Type {} can not be returned by a MCFunction.",
                type(ret_value)
            )
        )
    if MCF.do_gc:
        for shadow in MCF._context.values():
            if shadow._meta == 'norm':
                shadow.rm()
    ReturN().value(1)
