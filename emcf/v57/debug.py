
import traceback, os
from ..core import MCF, MCFCore
from .._writers import *
from ..types import MCFVariable
from typing import (
    Any
)

__all__ = [
    'log'
]

_work_root = os.getcwd()

def _init_helper(_core: MCFCore) -> None:
    _core.useComponent('debug', {
        "st": _core.storage
    })

def log(obj: Any, include_src: bool = True) -> None:
    if isinstance(obj, MCFVariable):
        obj.move("call.m0")
    else:
        Data.storage(MCF.storage).modify_set("call.m0").value(f'"{str(obj)}"')
    Function(MCF.builtinSign('debug.log')).call()
    if include_src:
        call_frame = traceback.extract_stack(limit=2)[-2]
        file, line, name, _ = call_frame
        file = os.path.relpath(file, _work_root).replace("\\", "/")
        Data.storage(MCF.storage).modify_set("call.m0").value(f'"{file}"')
        Data.storage(MCF.storage).modify_set("call.m1").value(f'"{line}"')
        Data.storage(MCF.storage).modify_set("call.m2").value(f'"{name}"')
        Function(MCF.builtinSign('debug.log_src')).with_args(
            Data.storage(MCF.storage), "call"
        )

MCF.initializeHelper(_init_helper)
