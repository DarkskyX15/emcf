
from .core import MCF
from .selector import Selector
from .types import MCFVariable
from typing import Any, TextIO

def say(obj: Any, target: Selector | None = None) -> None:

    def _write_say_macro(io: TextIO, select: str, sig: str) -> None:
        io.write(
f"""data modify storage {MCF.storage} call.m0 set value "{select}"
function {sig} with storage {MCF.storage} call
"""
        )
    
    def _write_no_macro(io: TextIO, select: str, text: str) -> None:
        io.write(
f"""execute as {select} run say {text}
"""
        )   

    if target is None:
        target = Selector("@s")
    
    MCF.exportComponent("display.say")

    with target:
        if isinstance(obj, MCFVariable):
            obj.move("call.m1")
            MCF.write(
                _write_say_macro,
                target.select(), MCF.builtinSign('display.say.main')
            )
        else:
            MCF.write(
                _write_no_macro,
                target.select(), str(obj)
            )
    
