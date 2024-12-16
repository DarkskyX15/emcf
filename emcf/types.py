
from .core import MCF
from .exceptions import *
from abc import abstractmethod
from typing import TypeAlias, NewType, Any, Union, TextIO

class MCFVariable:
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

Integer = NewType("Integer", MCFVariable)
IntegerConvertible: TypeAlias = Integer | int
class Integer(MCFVariable):
    _mcf_id: str

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
                "Can not use {} as initial value for Integer.",
                value
            )
        return self

    def move(self, dist: str) -> None:
        MCF.write(
            self._write_move,
            self._mcf_id, dist
        )

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
                "Can not multiple {} with an Integer.",
                other
            )
        return temp

    def __mul__(self, other: IntegerConvertible) -> Integer:
        return self._operation(other, '*')

    def __add__(self, other: IntegerConvertible) -> Integer:
        return self._operation(other, '+')
    
    def __sub__(self, other: IntegerConvertible) -> Integer:
        return self._operation(other, '-')
    
    def __floordiv__(self, other: IntegerConvertible) -> Integer:
        return self._operation(other, '/')
    
    def __mod__(self, other: IntegerConvertible) -> Integer:
        return self._operation(other, '%')

    def __del__(self):
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
    def _write_move(io: TextIO, this: str, dist: str) -> None:
        io.write(
f"""execute store result storage {MCF.storage} move.{dist} int 1.0 run scoreboard players get {this} {MCF.sb_general}
"""            
        )

