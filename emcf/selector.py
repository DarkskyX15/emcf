
from .core import MCF
from .exceptions import MCFVersionError, MCFValueError
from typing import TextIO

class Selector:
    _target: str
    _built: str
    _last_tag: str | None
    _with_limit: bool
    
    def __init__(self, target):
        self._target = target
        self._last_tag = None
        self._built = ''
        self._with_limit = False
        if target not in MCF.database.selectors:
            raise MCFVersionError(f"Selector {target} not supported")
        self._built += target

    def __enter__(self) -> str:
        self._last_tag = MCF.getFID()
        MCF.write(
            self._write_enter,
            self._built, self._last_tag
        )

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        MCF.write(
            self._write_leave,
            self._target, self._last_tag
        )

    def select(self) -> str:
        if self._last_tag is None:
            raise MCFValueError("select() called before tag specification.")
        return f"{self._target}[tag={self._last_tag}]"
    
    @staticmethod
    def _write_enter(io: TextIO, select: str, tag: str) -> None:
        io.write(
f"""tag {select} add {tag}
"""
        )
    
    @staticmethod
    def _write_leave(io: TextIO, target: str, tag: str) -> None:
        io.write(
f"""tag {target}[tag={tag}] remove {tag}
"""
        )
