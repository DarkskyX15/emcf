
from .core import MCF
from ._exceptions import MCFTypeError
from .types import MCFVariable, FakeNone
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
    _context: list

    def __init__(self, ret_type: Type[Ret] = FakeNone):
        self._entry_path, self._entry_sig = MCF.makeFunction()
        self._body_path, self._body_sig = MCF.makeFunction()
        self._ret_addr = MCF.getFID()
        self._exported = False
        self._ret_type = ret_type
        self._input_addr = []
        self._context = []

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
                raise MCFTypeError(
                    "Parameter '{}' can not be passed to a MCFunction.", arg
                )
        return tuple(collected)

    def _export_params(self, args: tuple[object]) -> None:
        index = 0
        for arg in args:
            if isinstance(arg, MCFVariable):
                MCF.write(
                    self._write_export,
                    arg._mcf_id, str(index)
                )
                index += 1
            else:
                raise MCFTypeError(
                    "Parameter '{}' can not be passed to a MCFunction.", arg
                )

    @staticmethod
    def _write_export(io: TextIO, this: str, idx: str) -> None:
        io.write(
f"""data modify storage {MCF.storage} call.m{idx} set value "{this}"
"""
        )

    @staticmethod
    def _write_call(io: TextIO, sig: str, params: str | None) -> None:
        if params is None:
            io.write(
f"""function {sig}
"""
            )
        else:
            io.write(
f"""function {sig} with storage {MCF.storage} {params}
"""
            )

    def _push_stack(self) -> None:
        index = 0
        for var in MCF._context:
            var.move(f"frame.m{index}")
            index += 1
        MCF.write(self._write_push_frame)
        MCF._context_stack.append(MCF._context[:])
        MCF._context.clear()
    
    @staticmethod
    def _write_push_frame(io: TextIO) -> None:
        io.write(
f"""data modify storage {MCF.storage} frame.cond_stack set from storage {MCF.storage} cond_stack
execute store result storage {MCF.storage} frame.terminate byte 1.0 run scoreboard players get {MCF.TERMINATE} {MCF.sb_sys}
data modify storage {MCF.storage} stack append from storage {MCF.storage} frame
data modify storage {MCF.storage} frame set value """ + "{}\n"
        )

    def _new_stack(self) -> None:
        MCF._context.extend(self._context)
        MCF.write(self._write_reset_frame)

    @staticmethod
    def _write_reset_frame(io: TextIO) -> None:
        io.write(
f"""data modify storage {MCF.storage} cond_stack set value []
scoreboard players set {MCF.TERMINATE} {MCF.sb_sys} 0
"""
        )

    def _pop_stack(self) -> None:
        MCF._context = MCF._context_stack.pop()
        MCF.write(self._write_pop_frame)
        index = 0
        for var in MCF._context:
            var.collect(f"frame.m{index}")
            index += 1

    @staticmethod
    def _write_pop_frame(io: TextIO) -> None:
        io.write(
f"""data modify storage {MCF.storage} frame set from storage {MCF.storage} stack[-1]
data remove storage {MCF.storage} stack[-1]
data modify storage {MCF.storage} cond_stack set from storage {MCF.storage} frame.cond_stack
execute store result score {MCF.TERMINATE} {MCF.sb_sys} run data get storage {MCF.storage} frame.terminate 1.0
"""
        )

    def __call__(self, func: Callable[[*Args], None]) -> Callable[[*Args], Ret]:
        @wraps(func)
        def wrapper(*args: *Args) -> Ret:
            if not self._exported:
                for _ in range(len(args)):
                    self._input_addr.append(MCF.getFID())

            self._push_stack()

            self._export_params(args)
            if not self._exported:
                self._exported = True
                MCF.forward(self._entry_path)
                collected = self._collect_params(args)
                for var in collected:
                    new = var.duplicate(None, True)
                    new._mcf_id = var._mcf_id
                    new._do_gc = False
                    self._context.append(new)
                self._new_stack()
                MCF.write(
                    self._write_call,
                    self._body_sig, None
                )

                MCF.forward(self._body_path)
                func(*collected)
                MCF.rewind()
                
                for var in collected:
                    var._do_gc = False
                del collected
                MCF.rewind()
            else:
                self._new_stack()

            MCF.write(
                self._write_call,
                self._entry_sig, "call"
            )

            ret_val = self._ret_type(None, False)
            if isinstance(ret_val, FakeNone):
                ret_val = None
                self._pop_stack()
            else:
                ret_val.collect("ret_val")
                self._pop_stack()
                shadow = ret_val.duplicate(None, True)
                shadow._mcf_id = ret_val._mcf_id
                shadow._do_gc = False
                MCF._context.append(shadow)
            
            return ret_val
        
        return wrapper

def Return(ret_value: MCFVariable = FakeNone()) -> None:
    def _write_return(io: TextIO, empty: bool):
        io.write(
f"""scoreboard players set {MCF.TERMINATE} {MCF.sb_sys} 1
"""
        )
        if empty:
            io.write(
f"""data modify storage {MCF.storage} ret_val set value ""
"""
            )
    def _write_end(io: TextIO):
        io.write("return 1\n")
    if isinstance(ret_value, FakeNone):
        MCF.write(_write_return, True)
    elif isinstance(ret_value, MCFVariable):
        MCF.write(_write_return, False)
        ret_value.move("ret_val")
    else:
        raise MCFTypeError(
            "Type {} can not be returned by a MCFunction.",
            type(ret_value)
        )
    for shadow in MCF._context:
        shadow.rm()
    MCF.write(_write_end)
