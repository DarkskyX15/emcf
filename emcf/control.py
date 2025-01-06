
from .core import MCF
from ._utils import console
from ._exceptions import MCFTypeError
from .types import Condition
from ._writers import *
from typing import TextIO, Self, Callable

__all__ = [
    'If',
    'Elif',
    'Else',
]

class ConditionControl:
    _enter: Callable
    _condition: Condition | None
    _func_path: str
    _func_sig: str
    
    def __init__(self, writer: Callable, condition: Condition | None):
        self._enter = writer
        self._condition = condition
        self._func_path, self._func_sig = MCF.makeFunction()

    def __enter__(self) -> Self:
        if self._condition is None:
            self._enter(self._func_sig)
        else:
            if not isinstance(self._condition, Condition):
                console.error(
                    MCFTypeError(
                        "Can not use {} as a condition.",
                        self._condition
                    )
                )
            else:
                self._enter(self._condition._mcf_id, self._func_sig)
        MCF.forward(self._func_path)
        return self
    
    def __exit__(self, type, value, traceback) -> None:
        MCF.rewind()
        Execute().store('result').score(MCF.COND_LAST, MCF.sb_sys).run(
            Data.storage(MCF.storage).get("cond_stack[-1]", 1.0)
        )
        Data.storage(MCF.storage).remove("cond_stack[-1]")
        Execute().condition('if').score_matches(
            MCF.TERMINATE, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(1)
        )

    @staticmethod
    def _write_if(that: str, sig: str) -> None:
        Execute().store('result').storage(
            MCF.storage, "register", 'byte', 1.0
        ).run(
            ScoreBoard.players_get(that, MCF.sb_general)
        )
        Data.storage(MCF.storage).modify_append("cond_stack").via(
            Data.storage(MCF.storage), "register"
        )
        Execute().condition('if').score_matches(
            that, MCF.sb_general, 1, 1
        ).run(
            Function(sig).call()
        )

    @staticmethod
    def _write_elif(that: str, sig: str) -> None:
        ScoreBoard.players_set(MCF.GENERAL, MCF.sb_sys, 0)
        Execute().condition('if').score_matches(
            MCF.COND_LAST, MCF.sb_sys, 0, 0
        ).condition('if').score_matches(
            that, MCF.sb_general, 1, 1
        ).run(
            ScoreBoard.players_set(MCF.GENERAL, MCF.sb_sys, 1)
        )
        Execute().condition('if').score_matches(
            MCF.GENERAL, MCF.sb_sys, 1, 1
        ).store('result').storage(
            MCF.storage, "register", 'byte', 1.0
        ).run(
            ScoreBoard.players_get(MCF.GENERAL, MCF.sb_sys)
        )
        Execute().condition('if').score_matches(
            MCF.GENERAL, MCF.sb_sys, 0, 0
        ).store('result').storage(
            MCF.storage, "register", 'byte', 1.0
        ).run(
            ScoreBoard.players_get(MCF.COND_LAST, MCF.sb_sys)
        )
        Data.storage(MCF.storage).modify_append("cond_stack").via(
            Data.storage(MCF.storage), "register"
        )
        Execute().condition('if').score_matches(
            MCF.GENERAL, MCF.sb_sys, 1, 1
        ).run(
            Function(sig).call()
        )

    @staticmethod
    def _write_else(sig: str) -> None:
        ScoreBoard.players_set(MCF.GENERAL, MCF.sb_sys, 0)
        Execute().condition('if').score_matches(
            MCF.COND_LAST, MCF.sb_sys, 0, 0
        ).run(
            ScoreBoard.players_set(MCF.GENERAL, MCF.sb_sys, 1)
        )
        Execute().store('result').storage(
            MCF.storage, "register", 'byte', 1.0
        ).run(
            ScoreBoard.players_get(MCF.GENERAL, MCF.sb_sys)
        )
        Data.storage(MCF.storage).modify_append("cond_stack").via(
            Data.storage(MCF.storage), "register"
        )
        Execute().condition('if').score_matches(
            MCF.GENERAL, MCF.sb_sys, 1, 1
        ).run(
            Function(sig).call()
        )

class If(ConditionControl):
    def __init__(self, condition: Condition):
        super().__init__(
            ConditionControl._write_if, condition
        )

class Elif(ConditionControl):
    def __init__(self, condition: Condition):
        super().__init__(
            ConditionControl._write_elif, condition
        )

class Else(ConditionControl):
    def __init__(self):
        super().__init__(
            ConditionControl._write_else, None
        )

class While:
    _used: bool

    def __init__(self):
        self._used = False

    def use(self, condition: Condition) -> Self:
        self._used = True
        return self
    
    def __enter__(self) -> Self:
        pass

    def __exit__(self, type, value, traceback) -> None:
        pass

class Range:
    pass
