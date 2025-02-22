
from ..core import MCF
from .selector import Selector
from ..types import MCFVariable
from .._writers import *
from typing import Any, TextIO

__all__ = [
    'say'
]

def say(obj: Any, target: Selector | None = None) -> None:
    if target is None:
        target = Selector("@s")
    
    MCF.useComponent("display.say", {})

    with target:
        if isinstance(obj, MCFVariable):
            obj.move("call.m1")
            Data.storage(MCF.storage).modify_set("call.m0").value(f'"{target.select()}"')
            Function(MCF.builtinSign('display.say.main')).with_args(
                Data.storage(MCF.storage), "call"
            )
        else:
            Execute().As(target.select()).run(Say(str(obj)))
