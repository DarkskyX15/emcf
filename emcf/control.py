
from .core import MCF, MCFWriter
from .types import Condition
from typing import TextIO, Self, Callable

class ConditionControl:
    _enter: MCFWriter
    _condition: Condition
    _func_path: str
    _func_sig: str
    
    def __init__(self, writer: MCFWriter, condition: Condition | None):
        self._enter = writer
        self._condition = condition
        self._func_path, self._func_sig = MCF.makeFunction()

    def __enter__(self) -> Self:
        if self._condition is None:
            MCF.write(
                self._enter, self._func_sig
            )
        else:
            MCF.write(
                self._enter, self._condition._mcf_id, self._func_sig
            )
        MCF.forward(self._func_path)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        MCF.rewind()
        MCF.write(self._write_pop)

    @staticmethod
    def _write_pop(io: TextIO) -> None:
        io.write(
f"""execute store result score {MCF.COND_LAST} {MCF.sb_sys} run data get storage {MCF.storage} cond_stack[-1] 1.0
data remove storage {MCF.storage} cond_stack[-1]
execute if score {MCF.TERMINATE} {MCF.sb_sys} matches 1 run return 1
"""
        )

    @staticmethod
    def _write_if(io: TextIO, that: str, sig: str) -> None:
        io.write(
f"""execute store result storage {MCF.storage} register byte 1.0 run scoreboard players get {that} {MCF.sb_general}
data modify storage {MCF.storage} cond_stack append from storage {MCF.storage} register
execute if score {that} {MCF.sb_general} matches 1 run function {sig}
"""
        )

    @staticmethod
    def _write_elif(io: TextIO, that: str, sig: str) -> None:
        io.write(
f"""scoreboard players set {MCF.GENERAL} {MCF.sb_sys} 0
execute if score {MCF.COND_LAST} {MCF.sb_sys} matches 0 if score {that} {MCF.sb_general} matches 1 run scoreboard players set {MCF.GENERAL} {MCF.sb_sys} 1
execute if score {MCF.GENERAL} {MCF.sb_sys} matches 1 run execute store result storage {MCF.storage} register byte 1.0 run scoreboard players get {MCF.GENERAL} {MCF.sb_sys}
execute if score {MCF.GENERAL} {MCF.sb_sys} matches 0 run execute store result storage {MCF.storage} register byte 1.0 run scoreboard players get {MCF.COND_LAST} {MCF.sb_sys}
data modify storage {MCF.storage} cond_stack append from storage {MCF.storage} register
execute if score {MCF.GENERAL} {MCF.sb_sys} matches 1 run function {sig}
"""
        )

    @staticmethod
    def _write_else(io: TextIO, sig: str) -> None:
        io.write(
f"""scoreboard players set {MCF.GENERAL} {MCF.sb_sys} 0
execute if score {MCF.COND_LAST} {MCF.sb_sys} matches 0 run scoreboard players set {MCF.GENERAL} {MCF.sb_sys} 1
execute store result storage {MCF.storage} register byte 1.0 run scoreboard players get {MCF.GENERAL} {MCF.sb_sys}
data modify storage {MCF.storage} cond_stack append from storage {MCF.storage} register
execute if score {MCF.GENERAL} {MCF.sb_sys} matches 1 run function {sig}
"""
        )

class Mif(ConditionControl):
    def __init__(self, condition: Condition):
        super().__init__(
            ConditionControl._write_if, condition
        )

class Melif(ConditionControl):
    def __init__(self, condition: Condition):
        super().__init__(
            ConditionControl._write_elif, condition
        )

class Melse(ConditionControl):
    def __init__(self):
        super().__init__(
            ConditionControl._write_else, None
        )
