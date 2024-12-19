
from .core import MCF
from ._exceptions import MCFTypeError
from .types import MCFVariable
from typing import Callable, TypeVar, TypeVarTuple, Generic, TextIO
from functools import update_wrapper

Ret = TypeVar('Ret')
Args = TypeVarTuple('Args')
class MCFunction(Generic[*Args, Ret]):
    _entry_path: str
    _entry_sig: str
    _body_path: str
    _body_sig: str
    _exported: bool
    _ret_addr: str | None
    _input_addr: list[str]
    _context: list
    _function: Callable[[*Args], Ret]

    def __init__(self, func: Callable[[*Args], Ret]):
        self._entry_path, self._entry_sig = MCF.makeFunction()
        self._body_path, self._body_sig = MCF.makeFunction()
        self._exported = False
        self._function = func
        self._ret_addr = None
        self._input_addr = []
        self._context = []
        update_wrapper(self, func)

    def _collect_params(self, args: tuple[*Args]) -> tuple[*Args]:
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

    def _export_params(self, args: tuple[*Args]) -> None:
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
f"""execute store result storage {MCF.storage} frame.cond int 1.0 run scoreboard players get {MCF.COND_LAST} {MCF.sb_sys}
data modify storage {MCF.storage} stack append from storage {MCF.storage} frame
data modify storage {MCF.storage} frame set value """ + "{}\n"
        )

    def _new_stack(self) -> None:
        MCF._context.extend(self._context)
        MCF.write(self._write_reset_frame)

    @staticmethod
    def _write_reset_frame(io: TextIO) -> None:
        io.write(
f"""scoreboard players set {MCF.COND_LAST} {MCF.sb_sys} 0
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
execute store result score {MCF.COND_LAST} {MCF.sb_sys} run data get storage {MCF.storage} frame.cond
"""
        )

    def __call__(self, *args: *Args) -> Ret:
        
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
            result = self._function(*collected)
            if result is None:
                pass
            elif isinstance(result, MCFVariable):
                self._ret_addr = result._mcf_id
            else:
                raise MCFTypeError(
                    "'{}' can not be returned by a MCFunction.",
                    result
                )
            MCF.rewind()
            for var in collected: del var
            del collected
            MCF.rewind()
        else:
            self._new_stack()

        MCF.write(
            self._write_call,
            self._entry_sig, "call"
        )

        self._pop_stack()
