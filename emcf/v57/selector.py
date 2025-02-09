
from ..core import MCF
from .._utils import console
from .._writers import *
from .._exceptions import MCFVersionError, MCFValueError
from typing import TextIO, Self

__all__ = [
    'Selector'
]

class Selector:
    _target: str
    _built: str
    _tag: str
    _in_context: bool
    _with_limit: bool
    
    def __init__(self, target):
        self._target = target
        self._tag = MCF.getFID()
        self._in_context = False
        self._built = ''
        self._with_limit = False
        if target not in MCF.database.selectors:
            console.error(
                MCFVersionError(
                    f"Selector {target} is not supported", MCF._mcf_version
                )
            )
        self._built += target

    def __enter__(self) -> Self:
        self._in_context = True
        Tag(self._built).add(self._tag)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        Tag(f"{self._target}[tag={self._tag}]").remove(self._tag)

    def select(self) -> str:
        if not self._in_context:
            console.error(
                MCFValueError("select() called without a selector context.")
            )
        return f"{self._target}[tag={self._tag}]"
    