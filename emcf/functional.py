
from .core import MCF
from ._exceptions import MCFTypeError
from .types import MCFVariable, FakeNone
from ._writers import *
from ._utils import console
from typing import Callable, TypeVar, TypeVarTuple, Generic, TextIO, Type
from functools import wraps

Ret = TypeVar('Ret')
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

    def __init__(self, ret_type: Type[Ret] = FakeNone):
        self._entry_path, self._entry_sig = MCF.makeFunction()
        self._body_path, self._body_sig = MCF.makeFunction()
        self._ret_addr = MCF.getFID()
        self._exported = False
        self._ret_type = ret_type
        self._input_addr = []
        self._context = {}

    def _collect_params(self, args: tuple[object]) -> tuple[MCFVariable]:
        collected = []
        index = 0
        for arg in args:
            if isinstance(arg, MCFVariable):
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

    def _new_stack(self) -> None:
        MCF._context.update(self._context)
        # 于此添加更多的栈帧默认值
        Data.storage(MCF.storage).modify_set("cond_stack").value("[]")
        Data.storage(MCF.storage).modify_set("loop_stack").value("[]")
        ScoreBoard.players_set(MCF.TERMINATE, MCF.sb_sys, 0)

    def _pop_stack(self) -> None:
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

    def __call__(self, func: Callable[[*Args], None]) -> Callable[[*Args], Ret]:
        @wraps(func)
        def wrapper(*args: *Args) -> Ret:
            if not self._exported:
                for _ in range(len(args)):
                    self._input_addr.append(MCF.getFID())       # 为每个参数生成一个Fool ID

            self._push_stack()              # 将当前上下文压入栈中

            valid = self._export_params(args)       # 将参数导出到存储中
            if not valid:
                console.error(
                    MCFTypeError(
                        "Failed to call function '{}' for it can not be converted to a MCFunction.",
                        func.__name__
                    )
                )

            if not self._exported and valid:        # 如果函数未导出，则导出函数
                self._exported = True
                MCF.forward(self._entry_path)
                collected = self._collect_params(args)      # 收集参数
                for var in collected:
                    var._gc_sign = 'shadow'
                    self._context[var._mcf_id] = var       # 储存为函数上下文
                self._new_stack()               # 更新当前上下文
                Function(self._body_sig).call()

                MCF.forward(self._body_path)
                func(*collected)                # 写函数内容
                MCF.rewind()
                
                if MCF.do_gc:
                    for var in collected:       # 清理函数收集的参数
                        var.rm()

                MCF.rewind()
            else:
                self._new_stack()       # 更新当前上下文

            Function(self._entry_sig).with_args(
                Data.storage(MCF.storage), "call"
            )

            ret_val = self._ret_type(None, False)
            if isinstance(ret_val, FakeNone):
                ret_val = None
                self._pop_stack()       # 恢复上下文
            else:
                ret_val.collect("ret_val")
                self._pop_stack()           # 恢复上下文
                MCF.addContext(ret_val)     # 将返回值添加至当前上下文
            
            return ret_val
        
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
            shadow.rm()
    ReturN().value(1)
