
from .core import MCF
from ._exceptions import *
from abc import abstractmethod
from typing import TypeAlias, NewType, Any, Union, TextIO

class MCFVariable:
    _mcf_id: str
    def __init__(self):
        pass
    @abstractmethod
    def move(self, dist: str) -> None:
        pass

def MCFFunction() -> None:
    pass

Register = NewType("Register", MCFVariable)
class Register(MCFVariable):
    _address: str
    def __init__(self, addr: str):
        super().__init__()
        self._address = addr

Condition = NewType("Condition", MCFVariable)
ConditionConvertible: TypeAlias = Condition | bool
class Condition(MCFVariable):
    def __init__(self, init_val: ConditionConvertible | None = False):
        super().__init__()
        self._mcf_id = MCF.registerValue()
        if init_val is None: return 
        self.assign(init_val)
    
    def assign(self, value: ConditionConvertible) -> Condition:
        if isinstance(value, bool):
            MCF.write(
                self._write_set,
                self._mcf_id, MCF.sb_general,
                '1' if value else '0'
            )
        elif isinstance(value, Condition):
            MCF.write(
                self._write_assign,
                self._mcf_id, MCF.sb_general,
                value._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not use {} as value for Condition.",
                value
            )

    @staticmethod
    def _write_set(io: TextIO, this: str, this_sb: str, value: str) -> None:
        io.write(
f"""scoreboard players set {this} {this_sb} {value}
"""
        )

    @staticmethod
    def _write_assign(
        io: TextIO,
        this: str, this_sb: str,
        that: str, that_sb: str
    ) -> None:
        io.write(
f"""scoreboard players operation {this} {this_sb} = {that} {that_sb}
"""
        )

    def move(self, dist: str) -> None:
        MCF.write(
            self._write_move,
            self._mcf_id, dist
        )

    @staticmethod
    def _write_move(io: TextIO, this: str, dist: str) -> None:
        io.write(
f"""execute store result storage {MCF.storage} move.{dist} int 1.0 run scoreboard players get {this} {MCF.sb_general}
"""            
        )

    def And(self, value: ConditionConvertible) -> Condition:
        temp = Condition(self)
        if isinstance(value, bool):
            if not value:
                MCF.write(
                    self._write_set,
                    temp._mcf_id, MCF.sb_general,
                    '0'
                )
            else:
                MCF.write(
                    self._write_set,
                    MCF.CALC_CONST, MCF.sb_sys,
                    '1'
                )
                MCF.write(
                    self._write_and_or,
                    temp._mcf_id, MCF.sb_general,
                    '<',
                    MCF.CALC_CONST, MCF.sb_sys
                )
        elif isinstance(value, Condition):
            MCF.write(
                self._write_and_or,
                temp._mcf_id, MCF.sb_general,
                '<',
                value._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with a Condition.",
                value
            )
        return temp
    
    def Or(self, value: ConditionConvertible) -> Condition:
        temp = Condition(self)
        if isinstance(value, bool):
            if value:
                MCF.write(
                    self._write_set,
                    temp._mcf_id, MCF.sb_general,
                    '1'
                )
            else:
                MCF.write(
                    self._write_set,
                    MCF.CALC_CONST, MCF.sb_sys,
                    '0'
                )
                MCF.write(
                    self._write_and_or,
                    temp._mcf_id, MCF.sb_general,
                    '>',
                    MCF.CALC_CONST, MCF.sb_sys
                )
        elif isinstance(value, Condition):
            MCF.write(
                self._write_and_or,
                temp._mcf_id, MCF.sb_general,
                '>',
                value._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with a Condition.",
                value
            )
        return temp

    @staticmethod
    def _write_and_or(
        io: TextIO,
        this: str, this_sb: str,
        ops: str,
        that: str, that_sb: str
    ) -> None:
        io.write(
f"""scoreboard players operation {this} {this_sb} {ops} {that} {that_sb}
"""
        )

    def Not(self) -> Condition:
        temp = Condition(self)
        MCF.write(
            self._write_not,
            temp._mcf_id, MCF.sb_general
        )
        return temp

    def reverse(self) -> Condition:
        MCF.write(
            self._write_not,
            self._mcf_id, MCF.sb_general
        )
        return self

    @staticmethod
    def _write_not(io: TextIO, this: str, this_sb: str) -> None:
        io.write(
f"""scoreboard players add {this} {this_sb} 1
scoreboard players set {MCF.CALC_CONST} {MCF.sb_sys} 2
scoreboard players operation {this} {this_sb} %= {MCF.CALC_CONST} {MCF.sb_sys}
"""
        )

    def __del__(self) -> None:
        if MCF.do_gc:
            MCF.write(
                self._write_rm,
                self._mcf_id, MCF.sb_general
            )
        MCF.deleteValue(self._mcf_id)
    
    @staticmethod
    def _write_rm(io: TextIO, this: str, this_sb: str) -> None:
        io.write(
f"""scoreboard players reset {this} {this_sb}
"""
        )
        

Integer = NewType("Integer", MCFVariable)
IntegerConvertible: TypeAlias = Integer | int
class Integer(MCFVariable):

    def __init__(self, init_val: IntegerConvertible | None = 0):
        super().__init__()
        self._mcf_id = MCF.registerValue()
        if init_val is None: return
        self.assign(init_val)

    def assign(self, value: IntegerConvertible) -> Integer:
        if isinstance(value, int):
            MCF.write(
                self._write_const_sb,
                self._mcf_id, MCF.sb_general,
                str(value)
            )
        elif isinstance(value, Integer):
            if not MCF.exist(value._mcf_id):
                raise MCFNameError(value._mcf_id)
            MCF.write(
                self._write_operation,
                self._mcf_id, MCF.sb_general,
                value._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not use {} as value for Integer.",
                value
            )
        return self

    def move(self, dist: str) -> None:
        MCF.write(
            self._write_move,
            self._mcf_id, dist
        )

    def __pos__(self) -> Integer:
        return Integer(self)

    def __neg__(self) -> Integer:
        temp = Integer(self)
        MCF.write(
            self._write_neg,
            MCF.CALC_CONST, MCF.sb_sys,
            temp._mcf_id, MCF.sb_general
        )
        return temp

    def __abs__(self) -> Integer:
        temp = Integer(self)
        MCF.write(
            self._write_abs,
            MCF.CALC_CONST, MCF.sb_sys,
            temp._mcf_id, MCF.sb_general
        )
        return temp

    def _operation(
        self,
        other: IntegerConvertible,
        ops: str
    ) -> Integer:
        temp = Integer(None)
        if isinstance(other, int):
            MCF.write(
                self._write_operation,
                temp._mcf_id, MCF.sb_general,
                self._mcf_id, MCF.sb_general
            )
            MCF.write(
                self._write_const_sb,
                MCF.CALC_CONST, MCF.sb_sys,
                str(other)
            )
            MCF.write(
                self._write_ops_between,
                temp._mcf_id, MCF.sb_general,
                ops,
                MCF.CALC_CONST, MCF.sb_sys
            )
        elif isinstance(other, Integer):
            MCF.write(
                self._write_operation,
                temp._mcf_id, MCF.sb_general,
                self._mcf_id, MCF.sb_general
            )
            MCF.write(
                self._write_ops_between,
                temp._mcf_id, MCF.sb_general,
                ops,
                other._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with an Integer.",
                other
            )
        return temp

    def _r_operation(
        self,
        left: IntegerConvertible,
        ops: str
    ) -> Integer:
        temp = Integer(None)
        if isinstance(left, int):
            MCF.write(
                self._write_const_sb,
                temp._mcf_id, MCF.sb_general,
                left
            )
            MCF.write(
                self._write_ops_between,
                temp._mcf_id, MCF.sb_general,
                ops,
                self._mcf_id, MCF.sb_general
            )
        elif isinstance(left, Integer):
            MCF.write(
                self._write_operation,
                temp._mcf_id, MCF.sb_general,
                left._mcf_id, MCF.sb_general
            )
            MCF.write(
                self._write_ops_between,
                temp._mcf_id, MCF.sb_general,
                ops,
                self._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with an Integer.",
                left
            )
        return temp

    def _i_operation(
        self,
        other: IntegerConvertible,
        ops: str
    ) -> None:
        if isinstance(other, int):
            if ops == '+' or ops == '-':
                MCF.write(
                    self._write_shortcut,
                    self._mcf_id, MCF.sb_general,
                    "add" if ops == '+' else "remove",
                    str(other)
                )
            else:
                MCF.write(
                    self._write_const_sb,
                    MCF.CALC_CONST, MCF.sb_sys,
                    str(other)
                )
                MCF.write(
                    self._write_ops_between,
                    self._mcf_id, MCF.sb_general,
                    ops,
                    MCF.CALC_CONST, MCF.sb_sys
                )
        elif isinstance(other, Integer):
            MCF.write(
                self._write_ops_between,
                self._mcf_id, MCF.sb_general,
                ops,
                other._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with an Integer.",
                other
            )

    def __iadd__(self, other: IntegerConvertible) -> Integer:
        try:
            self._i_operation(other, '+')
        except MCFTypeError:
            return NotImplemented
        return self
    
    def __isub__(self, other: IntegerConvertible) -> Integer:
        try:
            self._i_operation(other, '-')
        except MCFTypeError:
            return NotImplemented
        return self
    
    def __ifloordiv__(self, other: IntegerConvertible) -> Integer:
        try:
            self._i_operation(other, '/')
        except MCFTypeError:
            return NotImplemented
        return self
    
    def __imul__(self, other: IntegerConvertible) -> Integer:
        try:
            self._i_operation(other, '*')
        except MCFTypeError:
            return NotImplemented
        return self
    
    def __imod__(self, other: IntegerConvertible) -> Integer:
        try:
            self._i_operation(other, '%')
        except MCFTypeError:
            return NotImplemented
        return self

    def __mul__(self, other: IntegerConvertible) -> Integer:
        try:
            return self._operation(other, '*')
        except MCFTypeError:
            return NotImplemented

    def __rmul__(self, left: IntegerConvertible) -> Integer:
        return self * left

    def __add__(self, other: IntegerConvertible) -> Integer:
        try:
            return self._operation(other, '+')
        except MCFTypeError:
            return NotImplemented
    
    def __radd__(self, left: IntegerConvertible) -> Integer:
        return self + left

    def __sub__(self, other: IntegerConvertible) -> Integer:
        try:
            return self._operation(other, '-')
        except MCFTypeError:
            return NotImplemented
    
    def __rsub__(self, left: IntegerConvertible) -> Integer:
        try:
            return self._r_operation(left, '-')
        except MCFTypeError:
            return NotImplemented

    def __floordiv__(self, other: IntegerConvertible) -> Integer:
        try:
            return self._operation(other, '/')
        except MCFTypeError:
            return NotImplemented
    
    def __rfloordiv__(self, left: IntegerConvertible) -> Integer:
        try:
            return self._r_operation(left, '/')
        except MCFTypeError:
            return NotImplemented

    def __mod__(self, other: IntegerConvertible) -> Integer:
        try:
            return self._operation(other, '%')
        except MCFTypeError:
            return NotImplemented

    def __rmod__(self, left: IntegerConvertible) -> Integer:
        try:
            return self._r_operation(left, '%')
        except:
            return NotImplemented

    def __del__(self):
        if MCF.do_gc:
            MCF.write(
                self._write_rm,
                self._mcf_id, MCF.sb_general
            )
        MCF.deleteValue(self._mcf_id)

    @staticmethod
    def _write_const_sb(io: TextIO, this, sb, val) -> None:
        io.write(
f"""scoreboard players set {this} {sb} {val}
"""
        )
    
    @staticmethod
    def _write_operation(
        io: TextIO,
        this, this_sb,
        that, that_sb
    ) -> None:
        io.write(
f"""scoreboard players operation {this} {this_sb} = {that} {that_sb}
"""
        )

    @staticmethod
    def _write_ops_between(
        io: TextIO,
        this, this_sb,
        operator,
        that, that_sb
    ) -> None:
        io.write(
f"""scoreboard players operation {this} {this_sb} {operator}= {that} {that_sb}
"""
        )

    @staticmethod
    def _write_rm(
        io: TextIO,
        this, this_sb
    ) -> None:
        io.write(
f"""scoreboard players reset {this} {this_sb}
"""
        )

    @staticmethod
    def _write_shortcut(
        io: TextIO,
        this: str, this_sb: str,
        tp: str, val: str
    ) -> None:
        io.write(
f"""scoreboard players {tp} {this} {this_sb} {val}
"""
        )

    @staticmethod
    def _write_move(io: TextIO, this: str, dist: str) -> None:
        io.write(
f"""execute store result storage {MCF.storage} move.{dist} int 1.0 run scoreboard players get {this} {MCF.sb_general}
"""            
        )

    @staticmethod
    def _write_neg(
        io: TextIO,
        cst: str, cst_sb: str,
        this: str, this_sb: str
    ) -> None:
        io.write(
f"""scoreboard players set {cst} {cst_sb} -1
scoreboard players operation {this} {this_sb} *= {cst} {cst_sb}
"""
        )

    @staticmethod
    def _write_abs(
        io: TextIO,
        cst: str, cst_sb: str,
        this: str, this_sb: str
    ) -> None:
        io.write(
f"""scoreboard players set {cst} {cst_sb} -1
execute if score {this} {this_sb} matches ..-1 run scoreboard players operation {this} {this_sb} *= {cst} {cst_sb}
"""
        )

    def _compare(
        self,
        value: ConditionConvertible,
        const_cmp: str,
        cmp: str, 
        offset: int = 0,
        reverse: bool = False
    ) -> Condition:
        temp = Condition(reverse)
        if isinstance(value, int):
            MCF.write(
                self._write_const_cmp,
                self._mcf_id, MCF.sb_general,
                temp._mcf_id, MCF.sb_general,
                const_cmp.format(value + offset),
                reverse
            )
        elif isinstance(value, Integer):
            MCF.write(
                self._write_compare,
                self._mcf_id, MCF.sb_general,
                value._mcf_id, MCF.sb_general,
                temp._mcf_id, MCF.sb_general,
                cmp, reverse
            )
        else:
            raise MCFTypeError(
                "Can not compare between {} and Integer",
                value
            )
        return temp

    def __eq__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, "{}", "=")
        except MCFTypeError:
            return NotImplemented

    def __ne__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, "{}", "=", 0, True)
        except MCFTypeError:
            return NotImplemented

    def __le__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, "..{}", "<=")
        except MCFTypeError:
            return NotImplemented
    
    def __gt__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, "{}..", ">", 1)
        except MCFTypeError:
            return NotImplemented
    
    def __ge__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, "{}..", ">=")
        except MCFTypeError:
            return NotImplemented

    def __lt__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, "..{}", "<", -1)
        except MCFTypeError:
            return NotImplemented
    
    @staticmethod
    def _write_const_cmp(
        io: TextIO,
        this: str, this_sb: str,
        that: str, that_sb: str,
        cond: str, reverse: bool
    ) -> None:
        val = '0' if reverse else '1'
        io.write(
f"""execute if score {this} {this_sb} matches {cond} run scoreboard players set {that} {that_sb} {val}
"""
        )
    
    @staticmethod
    def _write_compare(
        io: TextIO,
        this: str, this_sb: str,
        that: str, that_sb: str,
        cond: str, cond_sb: str,
        cmp: str, reverse: bool
    ) -> None:
        val = '0' if reverse else '1'
        io.write(
f"""execute if score {this} {this_sb} {cmp} {that} {that_sb} run scoreboard players set {cond} {cond_sb} {val}
"""
        )

