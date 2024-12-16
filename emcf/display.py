
from .core import MCF
from .selector import Selector
from .types import MCFVariable
from typing import Any, TextIO

def say(obj: Any, target: Selector | None = None) -> None:

    def _write_macro(io: TextIO) -> None:
        io.write(
f"""$execute as $(m0) run say $(m1)
"""
        )

    def _write_say_macro(io: TextIO, select: str, sig: str) -> None:
        io.write(
f"""data modify storage {MCF.storage} call.m0 set value "{select}"
data modify storage {MCF.storage} call.m1 set from storage {MCF.storage} move.m1
function {sig} with storage {MCF.storage} call
"""
        )
    
    def _write_no_macro(io: TextIO, select: str, text: str) -> None:
        io.write(
f"""execute as {select} run say {text}
"""
        )   

    FUNC_ID = "display.say"

    if target is None:
        target = Selector("@s")
    func_sig = MCF._component_reg.get(FUNC_ID, None)
    if func_sig is None:
        # create display.say
        path, func_sig = MCF.makeFunction()
        MCF.forward(path)
        MCF.write(
            _write_macro
        )
        MCF.rewind()
        MCF._component_reg[FUNC_ID] = func_sig

    with target:
        if isinstance(obj, MCFVariable):
            obj.move("m1")
            MCF.write(
                _write_say_macro,
                target.select(), func_sig
            )
        else:
            MCF.write(
                _write_no_macro,
                target.select(), str(obj)
            )
    
