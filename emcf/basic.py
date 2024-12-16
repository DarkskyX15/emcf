
from .core import MCF
from abc import abstractmethod
from typing import TypeAlias, NewType, Any, Union, TextIO

class MCFException(BaseException):
    def __init__(self, *args):
        super().__init__(*args)

class MCFTypeError(MCFException):
    message: str
    def __init__(self, sign: str, val: Any):
        super().__init__(sign, val)
        self.message = sign.format(val)
    def __str__(self):
        return self.message

class MCFNameError(MCFException):
    message: str
    def __init__(self, val: str):
        super().__init__(val)
        self.message = f"MCF id not found: {val}"
    def __str__(self):
        return self.message

class MCFVariable:
    def __init__(self):
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

    def __init__(self, init_val: IntegerConvertible | Register):
        super().__init__()
        self._mcf_id = MCF.registerValue()
        self._assign(init_val)
        
    
    def _assign(self, val: IntegerConvertible | Register) -> None:
        if isinstance(val, int):
            MCF.write(
                self._write_const_sb,
                f"#{self._mcf_id}", MCF.sb_general,
                str(val)
            )
        elif isinstance(val, Integer):
            if not MCF.exist(val._mcf_id):
                raise MCFNameError(val._mcf_id)
            MCF.write(
                self._write_operation,
                f"#{self._mcf_id}", MCF.sb_general,
                f"#{val._mcf_id}", MCF.sb_general
            )
        elif isinstance(val, Register):
            MCF.write(
                self._write_operation,
                f"#{self._mcf_id}", MCF.sb_general,
                val._address, MCF.sb_sys
            )
        else:
            raise MCFTypeError(
                "Can not use {} as initial value for Integer.",
                val
            )

    def _operation(
        self,
        other: IntegerConvertible | Register,
        ops: str
    ) -> Register:
        if isinstance(other, int):
            MCF.write(
                self._write_operation,
                MCF.CALC_RES, MCF.sb_sys,
                f"#{self._mcf_id}", MCF.sb_general
            )
            MCF.write(
                self._write_const_sb,
                MCF.CALC_CONST, MCF.sb_sys,
                str(other)
            )
            MCF.write(
                self._write_ops_between,
                MCF.CALC_RES, MCF.sb_sys,
                ops,
                MCF.CALC_CONST, MCF.sb_sys
            )
        elif isinstance(other, Integer):
            MCF.write(
                self._write_operation,
                MCF.CALC_RES, MCF.sb_sys,
                f"#{self._mcf_id}", MCF.sb_general
            )
            MCF.write(
                self._write_ops_between,
                MCF.CALC_RES, MCF.sb_sys,
                ops,
                f"#{other._mcf_id}", MCF.sb_general
            )
        elif isinstance(other, Register):
            if Register._address != MCF.CALC_RES:
                MCF.write(
                    self._write_operation,
                    MCF.CALC_RES, MCF.sb_sys,
                    Register._address, MCF.sb_sys
                )
            MCF.write(
                self._write_ops_between,
                MCF.CALC_RES, MCF.sb_sys,
                ops,
                f"#{self._mcf_id}", MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not multiple {} with an Integer.",
                other
            )
        return Register(MCF.CALC_RES)

    def __mul__(self, other: IntegerConvertible | Register) -> Register:
        return self._operation(other, '*')

    def __del__(self):
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

