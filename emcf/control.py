
from .core import MCF
from ._utils import console
from ._exceptions import MCFTypeError, MCFSyntaxError, MCFValueError
from .types import Condition, Integer, IntegerConvertible
from ._writers import *
from ._writers import _Collector, _MultiCollector
from traceback import extract_stack
from typing import TextIO, Self, Callable, Any
import os

__all__ = [
    'If',
    'Elif',
    'Else',
    'While',
    'Break',
    'Continue',
    'Range'
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
        MCF._last_ctx_type = MCF._context_type.pop()
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
        Execute().condition('if').score_matches(
            MCF.LOOP_EXIT, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(1)
        )
        Execute().condition('if').score_matches(
            MCF.LOOP_CONT, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(1)
        )

    @staticmethod
    def _write_if(that: str, sig: str) -> None:
        MCF._context_type.append('if')
        MCF._last_ctx_type = 'norm'
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
        if MCF._last_ctx_type != 'if' and MCF._last_ctx_type != 'elif':
            console.error(
                MCFSyntaxError(
                    "elif used not after an elif or if context."
                )
            )
        MCF._context_type.append('elif')
        MCF._last_ctx_type = 'norm'
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
        if MCF._last_ctx_type != 'if' and MCF._last_ctx_type != 'elif':
            console.error(
                MCFSyntaxError(
                    "else used not after an elif or if context."
                )
            )
        MCF._context_type.append('else')
        MCF._last_ctx_type = 'norm'
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
    _have_with: bool
    _redirect: _MultiCollector
    _old_redirect: Any
    _condition: Condition
    _context_temp: dict[str, Any]
    _control_func_path: str
    _control_func_sig: str
    _main_path: str
    _main_sig: str
    _temporary: bool

    def __init__(self):
        self._redirect = _MultiCollector()
        self._used = False
        self._have_with = False
        self._old_redirect = MCF._io_redirect
        self._context_temp = MCF._context.copy()
        self._temporary = False
        self._control_func_path, self._control_func_sig = MCF.makeFunction()
        self._main_path, self._main_sig = MCF.makeFunction()
        # save to loop stack
        Data.storage(MCF.storage).modify_set("register").value(r"{}")
        ScoreBoard.to_storage(
            "register.exit", MCF.LOOP_EXIT, MCF.sb_sys, 1.0, 'byte'
        )
        ScoreBoard.to_storage(
            "register.skip", MCF.LOOP_CONT, MCF.sb_sys, 1.0, 'byte'
        )
        Data.storage(MCF.storage).modify_append("loop_stack").via(
            Data.storage(MCF.storage), "register"
        )
        # reset loop exit flg
        ScoreBoard.players_set(MCF.LOOP_EXIT, MCF.sb_sys, 0)

        Function(self._control_func_sig).call()
        
        # forward to loop entry
        MCF.forward(self._control_func_path)
        # check terminate flg
        Execute().condition('if').score_matches(
            MCF.TERMINATE, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(0)
        )
        # reset loop skip flg
        ScoreBoard.players_set(MCF.LOOP_CONT, MCF.sb_sys, 0)
        # check exit flg
        Execute().condition('if').score_matches(
            MCF.LOOP_EXIT, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(0)
        )
        MCF.redirect(self._redirect)

    def __call__(self, condition: Condition) -> Self:
        self._used = True
        MCF.redirect(self._old_redirect)
        if not isinstance(condition, Condition):
            console.error(
                MCFTypeError(
                    "Can not use {} as condition for While.", condition
                )
            )
        # check if the condition is temporary
        self._condition = condition
        if self._context_temp.get(condition._mcf_id, None) is None:
            self._temporary = True
        # write logic expression update
        for cmd in self._redirect._buffer_list:
            MCF.write(cmd, False)
        # check condition, call main body
        Execute().condition('if').score_matches(
            condition._mcf_id, MCF.sb_general, 1, 1
        ).run(
            Function(self._main_sig).call()
        )
        return self
    
    def __del__(self) -> None:
        if not self._used:
            console.error(
                MCFSyntaxError(
                    "While created but never used."
                )
            )
        elif not self._have_with:
            console.error(
                MCFSyntaxError(
                    "While used but have no loop body."
                )
            )

    def __enter__(self) -> Self:
        MCF.forward(self._main_path)
        MCF._context_type.append('loop')
        MCF._last_ctx_type = 'norm'
        return self

    def __exit__(self, type, value, traceback) -> None:
        self._have_with = True
        MCF._last_ctx_type = MCF._context_type.pop()
        # return to entry
        MCF.rewind()
        Execute().condition('if').score_matches(
            self._condition._mcf_id, MCF.sb_general, 1, 1
        ).run(
            Function(self._control_func_sig).call()
        )
        # return to outer context
        MCF.rewind()
        # remove temporary condition variable
        if self._temporary: del self._condition
        # recover loop stack
        ScoreBoard.from_storage(
            "loop_stack[-1].exit", MCF.LOOP_EXIT, MCF.sb_sys, 1.0
        )
        ScoreBoard.from_storage(
            "loop_stack[-1].skip", MCF.LOOP_CONT, MCF.sb_sys, 1.0
        )
        Data.storage(MCF.storage).remove("loop_stack[-1]")
        # check terminate flg
        Execute().condition('if').score_matches(
            MCF.TERMINATE, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(0)
        )

class Range:
    
    _used: bool
    _index: Integer
    _step: Integer
    _last: Integer
    _positive: Condition
    _context: tuple[str]
    _control_path: str
    _control_sig: str
    _main_path: str
    _main_sig: str

    def __init__(self, *args: IntegerConvertible):
        stack = extract_stack()
        self._context = tuple(stack[-2])
        self._used = False

        def _type_reduction(arg: IntegerConvertible) -> Integer:
            if isinstance(arg, int):
                return Integer(arg)
            elif isinstance(arg, Integer):
                return Integer(arg)
            else:
                console.error(
                    MCFTypeError(
                        "Parameters for Range should be an Integer or int, not {}",
                        type(arg)
                    )
                )
                return Integer(0)

        self._positive = Condition(True)
        if len(args) == 1:
            self._index = _type_reduction(0)
            self._last = _type_reduction(args[0])
            self._step = _type_reduction(1)
        elif len(args) == 2:
            self._index = _type_reduction(args[0])
            self._last = _type_reduction(args[1])
            self._step = _type_reduction(1)
        elif len(args) == 3:
            self._index = _type_reduction(args[0])
            self._last = _type_reduction(args[1])
            self._step = _type_reduction(args[2])
            Execute().condition('if').score_matches(
                self._step._mcf_id, MCF.sb_general, None, -1
            ).run(
                ScoreBoard.players_set(
                    self._positive._mcf_id, MCF.sb_general, 0
                )
            )
        else:
            console.error(
                MCFValueError(
                    f"Range expects 1, 2 or 3 arguments, not {len(args)}"
                )
            )

        self._control_path, self._control_sig = MCF.makeFunction()
        self._main_path, self._main_sig = MCF.makeFunction()
        

    def __del__(self):
        if not self._used:
            console.warn(
                "Range object (in {}, line {}) created but never used.".format(
                    os.path.split(self._context[0])[1], self._context[1]
                )
            )

    def __iter__(self) -> Self:
        # save to loop stack
        Data.storage(MCF.storage).modify_set("register").value(r"{}")
        ScoreBoard.to_storage(
            "register.exit", MCF.LOOP_EXIT, MCF.sb_sys, 1.0, 'byte'
        )
        ScoreBoard.to_storage(
            "register.skip", MCF.LOOP_CONT, MCF.sb_sys, 1.0, 'byte'
        )
        Data.storage(MCF.storage).modify_append("loop_stack").via(
            Data.storage(MCF.storage), "register"
        )
        # reset loop exit flg
        ScoreBoard.players_set(MCF.LOOP_EXIT, MCF.sb_sys, 0)
        # entry
        Function(self._control_sig).call()
        MCF.forward(self._control_path)
        # check terminate flg
        Execute().condition('if').score_matches(
            MCF.TERMINATE, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(0)
        )
        # check break flg
        Execute().condition('if').score_matches(
            MCF.LOOP_EXIT, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(0)
        )
        ScoreBoard.players_set(MCF.LOOP_CONT, MCF.sb_sys, 0)
        Execute().condition('if').score_matches(
            self._positive._mcf_id, MCF.sb_general, 1, 1
        ).condition('if').score_compare(
            self._index._mcf_id, MCF.sb_general, ">=",
            self._last._mcf_id, MCF.sb_general
        ).run(
            ReturN().value(1)
        )
        Execute().condition('if').score_matches(
            self._positive._mcf_id, MCF.sb_general, 0, 0
        ).condition('if').score_compare(
            self._index._mcf_id, MCF.sb_general, "<=",
            self._last._mcf_id, MCF.sb_general
        ).run(
            ReturN().value(1)
        )
        # call main
        Function(self._main_sig).call()
        MCF.forward(self._main_path)
        MCF._context_type.append('loop')
        MCF._last_ctx_type = 'norm'
        return self

    def __next__(self) -> Integer:
        if self._used:
            # leave
            MCF.rewind()
            ScoreBoard.players_operation(
                self._index._mcf_id, MCF.sb_general, "+=",
                self._step._mcf_id, MCF.sb_general
            )
            Function(self._control_sig).call()
            MCF._last_ctx_type = MCF._context_type.pop()
            MCF.rewind()
            # recover loop stack
            ScoreBoard.from_storage(
                "loop_stack[-1].exit", MCF.LOOP_EXIT, MCF.sb_sys, 1.0
            )
            ScoreBoard.from_storage(
                "loop_stack[-1].skip", MCF.LOOP_CONT, MCF.sb_sys, 1.0
            )
            Data.storage(MCF.storage).remove("loop_stack[-1]")
            # do gc
            del self._index, self._last, self._positive, self._step
            # check terminate flg
            Execute().condition('if').score_matches(
                MCF.TERMINATE, MCF.sb_sys, 1, 1
            ).run(
                ReturN().value(0)
            )
            raise StopIteration
        self._used = True
        return self._index


def Break():
    if 'loop' not in MCF._context_type:
        console.error(
            MCFSyntaxError(
                "Break used out of a loop context."
            )
        )
    ReturN().run(
        ScoreBoard.players_set(
            MCF.LOOP_EXIT, MCF.sb_sys, 1
        )
    )

def Continue():
    if 'loop' not in MCF._context_type:
        console.error(
            MCFSyntaxError(
                "Continue used out of a loop context."
            )
        )
    ReturN().run(
        ScoreBoard.players_set(
            MCF.LOOP_CONT, MCF.sb_sys, 1
        )
    )
