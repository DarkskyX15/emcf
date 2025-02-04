"""
MCF所有基础变量的封装
"""

from .core import MCF, GCSign
from ._utils import console, iterable
from ._exceptions import *
from ._writers import *
from ._components import builtin_components as built_cps
from typing import (
    TypeAlias, Any, Union, TextIO, Self, Literal, Iterable,
    Generic, TypeVar, Annotated, get_origin, get_args,
    ClassVar, overload, Optional
)


__all__ = [
    'MCFVariable',
    'FakeNone',
    'Condition',
    'Integer',
    'Float',
    'ArrayList',
    'Long',
    'Int',
    'Byte',
    'Text'
]


# BaseClass

class MCFVariable:
    """MCF变量的基类

    所有的内置MCF变量都需要直接继承自`MCFVariable`
    """
    _mcf_id: str
    _gc_sign: GCSign
    _var_meta: str

    def __init__(self, init_val: Any, void: bool):
        """初始化MCF变量

        - `init_val`: 初始值
        - `void`: 是否为空值

        当初始值设置为`None`时，将不会做初始的赋值操作。因此，创建一个初始值为`None`
        的MCF变量将不会体现在生成的函数内，但是该变量会被记录至当前的上下文，
        且会生成Fool ID。

        当`void`参数为`True`时，创建的该MCF变量成为“空值”。空值将不会做初始化，不
        创建Fool ID，且不会被记录至当前的上下文。目前空值仅在上下文列表中使用，列表
        中空值的`_gc_sign`属性被设为`shadow`，防止重复析构的同时保留类型的操作。
        """
        self._var_meta = 'norm'
        self._gc_sign = 'norm' if MCF.do_gc else 'none'
        if not void:
            self._mcf_id = MCF.getFID()
            MCF.addContext(self)
            if init_val is not None:
                self.assign(init_val)

    def __del__(self) -> None:
        if self._gc_sign != 'shadow':
            MCF.removeContext(self)
        if self._gc_sign == 'norm' and not MCF.stop_gc:
            self.rm()

    def assign(self, value: Any):
        """将`value`赋值至自身"""
        raise NotImplementedError

    def move(self, dist: str):
        """将变量移动至storage的`dist`位置"""
        raise NotImplementedError

    def collect(self, src: str):
        """从storage的`src`位置收集数据"""
        raise NotImplementedError

    def extract(self, dist: str):
        """将变量解包至storage的`dist`位置。与`move`方法不同的是，`extract`产生的
        值可以直接用于nbt中，而不是与`move`一样移动变量整个的实现结构。
        """
        raise NotImplementedError

    def construct(self, src):
        """依靠storage的`src`路径处的数据创建变量。与`collect`方法不同的是，
        `collect`依赖的数据必须有完整的数据结构，而`construct`可直接从nbt值上创建变量。
        """
        raise NotImplementedError

    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> 'MCFVariable':
        """从`slot`指定的宏位置创建Fool ID为`mcf_id`的实例，
        但不保存至上下文。
        """
        raise NotImplementedError

    @staticmethod
    def duplicate(
        init_val: Any = None,
        void: bool = False
    ) -> 'MCFVariable':
        """产生与自身类型相同的对象"""
        raise NotImplementedError

    def rm(self):
        """写清除指令，但不将自身移出上下文"""
        raise NotImplementedError


# FakeNone

class FakeNone(MCFVariable):
    """虚假的None类型，用于表示MCFunction中的无返回值。

    该类仅初始化为空值。
    """
    def __init__(
        self, 
        init_val: Any = None, 
        void: bool = True
    ):
        super().__init__(None, True)
    
    @staticmethod
    def duplicate(
        init_val: Any = None,
        void: bool = True
    ) -> 'FakeNone':
        return FakeNone(None, True)

    # 不做回收处理
    def __del__(self):
        pass


# Condition Implementation

ConditionConvertible: TypeAlias = 'Condition | bool'
class Condition(MCFVariable):
    """布尔值类型"""
    def __init__(
        self,
        init_val: 'ConditionConvertible | None' = False,
        void: bool = False
    ):
        super().__init__(init_val, void)

    def assign(self, value: ConditionConvertible) -> None:
        """向布尔值赋值，可使用`Condition`或`bool`类型。"""
        if isinstance(value, bool):
            ScoreBoard.players_set(
                self._mcf_id,
                MCF.sb_general,
                '1' if value else '0'
            )
        elif isinstance(value, Condition):
            ScoreBoard.players_operation(
                self._mcf_id, MCF.sb_general,
                '=', value._mcf_id, MCF.sb_general
            )
        else:
            console.error(
                MCFTypeError(
                    "Can not use {} as value for Condition.",
                    value
                )
            )

    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> 'Condition':
        temp = Condition(None, True)
        temp._mcf_id = mcf_id
        ScoreBoard.players_operation(
            temp._mcf_id, MCF.sb_general, '=',
            f'$({slot})', MCF.sb_general,
            macro=True
        )
        return temp

    @staticmethod
    def duplicate(
        init_val: 'ConditionConvertible | None' = False,
        void: bool = False
    ) -> 'Condition':
        return Condition(init_val, void)

    def move(self, dist: str) -> None:
        ScoreBoard.to_storage(
            dist, self._mcf_id, MCF.sb_general, 1.0
        )

    def collect(self, src: str) -> None:
        ScoreBoard.from_storage(
            src, self._mcf_id, MCF.sb_general, 1.0
        )

    def extract(self, dist: str) -> None:
        ScoreBoard.to_storage(
            dist, self._mcf_id, MCF.sb_general, 1.0, 'byte'
        )

    def construct(self, src: str) -> None:
        ScoreBoard.from_storage(
            src, self._mcf_id, MCF.sb_general, 1.0
        )

    def And(self, value: ConditionConvertible) -> 'Condition':
        """与另一`Condition`或`bool`做逻辑与操作，返回新布尔值"""
        temp = Condition(self)
        if isinstance(value, bool):
            if not value:
                ScoreBoard.players_set(
                    temp._mcf_id, MCF.sb_general, '0'
                )
            else:
                ScoreBoard.players_set(
                    MCF.CALC_CONST, MCF.sb_sys, '1'
                )
                ScoreBoard.players_operation(
                    temp._mcf_id, MCF.sb_general, '<',
                    MCF.CALC_CONST, MCF.sb_sys
                )
        elif isinstance(value, Condition):
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, '<',
                value._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with a Condition.",
                value
            )
        return temp

    def Or(self, value: ConditionConvertible) -> 'Condition':
        """与另一`Condition`或`bool`做逻辑或操作，返回新布尔值"""
        temp = Condition(self)
        if isinstance(value, bool):
            if value:
                ScoreBoard.players_set(temp._mcf_id, MCF.sb_general, '1')
            else:
                ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, '0')
                ScoreBoard.players_operation(
                    temp._mcf_id, MCF.sb_general, '>',
                    MCF.CALC_CONST, MCF.sb_sys
                )
        elif isinstance(value, Condition):
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, '>',
                value._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with a Condition.",
                value
            )
        return temp

    def Not(self) -> 'Condition':
        """返回值与自身逻辑非后值一致的新布尔值"""
        temp = Condition(self)
        self._not(temp._mcf_id)
        return temp

    def Reverse(self) -> None:
        """对自身做逻辑非，无返回值"""
        self._not(self._mcf_id)

    def _not(self, this: str) -> None:
        ScoreBoard.players_add(this, MCF.sb_general, 1)
        ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, 2)
        ScoreBoard.players_operation(
            this, MCF.sb_general, "%=", MCF.CALC_CONST, MCF.sb_sys
        )

    def rm(self) -> None:
        ScoreBoard.players_reset(self._mcf_id, MCF.sb_general)


# Integer Implementation

IntegerConvertible: TypeAlias = 'Integer | int'
class Integer(MCFVariable):

    def __init__(
        self,
        init_val: 'IntegerConvertible | Float | None' = 0,
        void: bool = False
    ):
        super().__init__(init_val, void)

    def assign(self, value: 'IntegerConvertible | Float') -> None:
        if isinstance(value, int):
            ScoreBoard.players_set(self._mcf_id, MCF.sb_general, value)
        elif isinstance(value, Integer):
            ScoreBoard.players_operation(
                self._mcf_id, MCF.sb_general, "=",
                value._mcf_id, MCF.sb_general
            )
        elif isinstance(value, Float):
            value.extract("register")
            ScoreBoard.from_storage(
                "register", self._mcf_id, MCF.sb_general, 1.0
            )
        else:
            console.error(
                MCFTypeError(
                    "Can not use {} as value for Integer.",
                    value
                )
            )

    def rm(self) -> None:
        ScoreBoard.players_reset(self._mcf_id, MCF.sb_general)

    def move(self, dist: str) -> None:
        ScoreBoard.to_storage(
            dist, self._mcf_id, MCF.sb_general, 1.0
        )

    def collect(self, src: str) -> None:
        ScoreBoard.from_storage(
            src, self._mcf_id, MCF.sb_general, 1.0
        )

    def extract(self, dist: str, _type: IntegerVariableTypes = 'int') -> None:
        ScoreBoard.to_storage(
            dist, self._mcf_id, MCF.sb_general, 1.0, _type
        )

    def construct(self, src: str) -> None:
        ScoreBoard.from_storage(
            src, self._mcf_id, MCF.sb_general, 1.0
        )

    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> 'Integer':
        temp = Integer(None, True)
        temp._mcf_id = mcf_id
        ScoreBoard.players_operation(
            temp._mcf_id, MCF.sb_general, "=",
            f"$({slot})", MCF.sb_general,
            macro=True
        )
        return temp

    @staticmethod
    def duplicate(
        init_val: 'IntegerConvertible | None' = 0,
        void: bool = False
    ) -> 'Integer':
        return Integer(init_val, void)

    def __pos__(self) -> 'Integer':
        return Integer(self)

    def __neg__(self) -> 'Integer':
        temp = Integer(self)
        ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, -1)
        ScoreBoard.players_operation(
            temp._mcf_id, MCF.sb_general, "*=",
            MCF.CALC_CONST, MCF.sb_sys
        )
        return temp

    def __abs__(self) -> 'Integer':
        temp = Integer(self)
        ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, '-1')
        Execute().condition('if').score_matches(
            temp._mcf_id, MCF.sb_general, None, -1
        ).run(
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, "*=",
                MCF.CALC_CONST, MCF.sb_sys
            )
        )
        return temp

    def _operation(
        self,
        other: IntegerConvertible,
        ops: str
    ) -> 'Integer':
        temp = Integer(None)
        if isinstance(other, int):
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, "=",
                self._mcf_id, MCF.sb_general
            )
            ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, other)
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, f"{ops}=",
                MCF.CALC_CONST, MCF.sb_sys
            )
        elif isinstance(other, Integer):
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, "=",
                self._mcf_id, MCF.sb_general
            )
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, f"{ops}=",
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
    ) -> 'Integer':
        temp = Integer(None)
        if isinstance(left, int):
            ScoreBoard.players_set(temp._mcf_id, MCF.sb_general, left)
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, f"{ops}=",
                self._mcf_id, MCF.sb_general
            )
        elif isinstance(left, Integer):
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, "=",
                left._mcf_id, MCF.sb_general
            )
            ScoreBoard.players_operation(
                temp._mcf_id, MCF.sb_general, f"{ops}=",
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
            if ops == '+':
                ScoreBoard.players_add(self._mcf_id, MCF.sb_general, other)
            elif ops == '-':
                ScoreBoard.players_remove(self._mcf_id, MCF.sb_general, other)
            else:
                ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, other)
                ScoreBoard.players_operation(
                    self._mcf_id, MCF.sb_general, f"{ops}=",
                    MCF.CALC_CONST, MCF.sb_sys
                )
        elif isinstance(other, Integer):
            ScoreBoard.players_operation(
                self._mcf_id, MCF.sb_general, f"{ops}=",
                other._mcf_id, MCF.sb_general
            )
        else:
            raise MCFTypeError(
                "Can not operate {} with an Integer.",
                other
            )

    def __iadd__(self, other: IntegerConvertible) -> 'Integer':
        try:
            self._i_operation(other, '+')
        except MCFTypeError:
            return NotImplemented
        return self

    def __isub__(self, other: IntegerConvertible) -> 'Integer':
        try:
            self._i_operation(other, '-')
        except MCFTypeError:
            return NotImplemented
        return self

    def __ifloordiv__(self, other: IntegerConvertible) -> 'Integer':
        try:
            self._i_operation(other, '/')
        except MCFTypeError:
            return NotImplemented
        return self

    def __imul__(self, other: IntegerConvertible) -> 'Integer':
        try:
            self._i_operation(other, '*')
        except MCFTypeError:
            return NotImplemented
        return self

    def __imod__(self, other: IntegerConvertible) -> 'Integer':
        try:
            self._i_operation(other, '%')
        except MCFTypeError:
            return NotImplemented
        return self

    def __mul__(self, other: IntegerConvertible) -> 'Integer':
        try:
            return self._operation(other, '*')
        except MCFTypeError:
            return NotImplemented

    def __rmul__(self, left: IntegerConvertible) -> 'Integer':
        return self * left

    def __add__(self, other: IntegerConvertible) -> 'Integer':
        try:
            return self._operation(other, '+')
        except MCFTypeError:
            return NotImplemented

    def __radd__(self, left: IntegerConvertible) -> 'Integer':
        return self + left

    def __sub__(self, other: IntegerConvertible) -> 'Integer':
        try:
            return self._operation(other, '-')
        except MCFTypeError:
            return NotImplemented

    def __rsub__(self, left: IntegerConvertible) -> 'Integer':
        try:
            return self._r_operation(left, '-')
        except MCFTypeError:
            return NotImplemented

    def __floordiv__(self, other: IntegerConvertible) -> 'Integer':
        try:
            return self._operation(other, '/')
        except MCFTypeError:
            return NotImplemented

    def __rfloordiv__(self, left: IntegerConvertible) -> 'Integer':
        try:
            return self._r_operation(left, '/')
        except MCFTypeError:
            return NotImplemented

    def __mod__(self, other: IntegerConvertible) -> 'Integer':
        try:
            return self._operation(other, '%')
        except MCFTypeError:
            return NotImplemented

    def __rmod__(self, left: IntegerConvertible) -> 'Integer':
        try:
            return self._r_operation(left, '%')
        except:
            return NotImplemented


    def _compare(
        self,
        value: IntegerConvertible,
        index: list[int],
        compare: str,
        offset: int = 0,
        reverse: bool = False
    ) -> Condition:
        temp = Condition(False)
        if isinstance(value, int):
            cmp_range: list[int | None] = [None, None]
            for idx in index:
                cmp_range[idx] = value + offset
            Execute().condition(
                'unless' if reverse else 'if'
            ).score_matches(
                self._mcf_id, MCF.sb_general, cmp_range[0],
                cmp_range[1]
            ).run(
                ScoreBoard.players_set(
                    temp._mcf_id, MCF.sb_general, 1
                )
            )
        elif isinstance(value, Integer):
            Execute().condition(
                'unless' if reverse else 'if'
            ).score_compare(
                self._mcf_id, MCF.sb_general, compare,
                value._mcf_id, MCF.sb_general
            ).run(
                ScoreBoard.players_set(
                    temp._mcf_id, MCF.sb_general, 1
                )
            )
        else:
            raise MCFTypeError(
                "Can not compare between {} and Integer",
                value
            )
        return temp

    def __eq__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, [0, 1], "=", 0, False)
        except MCFTypeError:
            return NotImplemented

    def __ne__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, [0, 1], "=", 0, True)
        except MCFTypeError:
            return NotImplemented

    def __le__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, [1], "<=", 0, False)
        except MCFTypeError:
            return NotImplemented

    def __gt__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, [0], ">", 1, False)
        except MCFTypeError:
            return NotImplemented

    def __ge__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, [0], ">=", 0, False)
        except MCFTypeError:
            return NotImplemented

    def __lt__(self, value: IntegerConvertible) -> Condition:
        try:
            return self._compare(value, [1], "<", -1, False)
        except MCFTypeError:
            return NotImplemented


# Float Implementation

FloatConvertible: TypeAlias = 'Float | float | int'
class Float(MCFVariable):
    def __init__(
        self,
        init_val: 'FloatConvertible | Integer | None' = 0.0,
        void: bool = False
    ):
        super().__init__(init_val, void)
        MCF.useComponent('math.float.compare', built_cps.float_compare)
        MCF.useComponent('math.float.extract', built_cps.float_extract)
        MCF.useComponent('math.float.compute', built_cps.float_compute)
        MCF.useComponent('math.float.construct', built_cps.float_construct)
        MCF.useComponent('math.pow10', built_cps.math_pow10)
    
    @staticmethod
    def _extract_float(f: float) -> tuple[int, int, int]:
        f_str = "{:.8e}".format(f)
        front, back = f_str.split('e')
        for idx in range(len(front) - 1, -1, -1):
            if front[idx] != '0':
                break
        size = idx
        front = front[:idx + 1]
        back = int(back)
        front = front.split('.')
        front = int(front[0] + front[1])
        if f < 0.0: size -= 1
        return (front, back, size)

    def assign(self, value: 'FloatConvertible | Integer') -> None:
        if isinstance(value, int):
            value = float(value)
        if isinstance(value, float):
            a, e, v = self._extract_float(value)
            if a == 0: v = 0
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(
                '{' + f"a:{a},e:{e}b,v:{v}b" + '}'
            )
        elif isinstance(value, Float):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
                Data.storage(MCF.storage), f"mem.{value._mcf_id}"
            )
        elif isinstance(value, Integer):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value("{}")
            value.move("register")
            Function(MCF.builtinSign('math.float.construct.make')).call()
            ScoreBoard.to_storage(
                f"mem.{self._mcf_id}.a", MCF.GENERAL, MCF.sb_sys, 1.0, 'int'
            )
            ScoreBoard.to_storage(
                f"mem.{self._mcf_id}.e", MCF.BUFFER1, MCF.sb_sys, 1.0, 'byte'
            )
            ScoreBoard.to_storage(
                f"mem.{self._mcf_id}.v", MCF.BUFFER2, MCF.sb_sys, 1.0, 'byte'
            )
        else:
            console.error(
                MCFTypeError(
                    "Can not use {} as value for Float.",
                    value
                )
            )
    
    def move(self, dist: str) -> None:
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )

    def collect(self, src: str) -> None:
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), src
        )

    def construct(self, src: str) -> None:
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value("{}")
        Data.storage(MCF.storage).modify_set("register").via(
            Data.storage(MCF.storage), src
        )
        Function(MCF.builtinSign('math.float.construct.make')).call()
        ScoreBoard.to_storage(
            f"mem.{self._mcf_id}.a", MCF.GENERAL, MCF.sb_sys, 1.0, 'int'
        )
        ScoreBoard.to_storage(
            f"mem.{self._mcf_id}.e", MCF.BUFFER1, MCF.sb_sys, 1.0, 'byte'
        )
        ScoreBoard.to_storage(
            f"mem.{self._mcf_id}.v", MCF.BUFFER2, MCF.sb_sys, 1.0, 'byte'
        )

    def extract(self, dist: str, _type: FloatingPointVariableTypes = 'float') -> None:
        self.move("register")
        Data.storage(MCF.storage).modify_set("call.m0").value(f'"{_type}"')
        Function(MCF.builtinSign(f'math.float.extract.run')).call()
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), "register"
        )

    @staticmethod
    def duplicate(
        init_val: 'FloatConvertible | None' = 0.0,
        void: bool = False
    ) -> 'Float':
        return Float(init_val, void)
    
    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> 'Float':
        temp = Float(None, True)
        temp._mcf_id = mcf_id
        Data.storage(MCF.storage).modify_set(f"mem.{mcf_id}", True).via(
            Data.storage(MCF.storage), f"mem.$({slot})"
        )
        return temp

    @staticmethod
    def _type_reduction(other: FloatConvertible) -> 'Float':
        reduced = float(other) if isinstance(other, int) else other
        if not isinstance(reduced, float) and not isinstance(reduced, Float):
            raise MCFTypeError("Can not operate {} with a Float.", other)
        reduced = Float(reduced) if isinstance(reduced, float) else reduced
        return reduced

    @staticmethod
    def _operate(left: 'Float', right: 'Float', ops: str) -> 'Float':
        temp = Float(None, False)
        left.move("cache.left")
        right.move("cache.right")
        if ops == '+' or ops == '-':
            branch = 'plus' if ops == '+' else 'sub'
            Function(
                MCF.builtinSign(f"math.float.compute.run_{branch}")
            ).call()
            temp.collect("register")
        elif ops == '*' or ops == '/':
            branch = 'mul' if ops == '*' else 'div'
            Function(
                MCF.builtinSign(f"math.float.compute.run_{branch}")
            ).call()
            temp.collect("register")
        else:
            raise MCFTypeError(
                "Unsupported operation type '{}' for Float.", ops
            )
        return temp

    def _operation(self, other: FloatConvertible, ops: str) -> 'Float':
        target = Float._type_reduction(other)
        temp = Float._operate(self, target, ops)
        return temp

    def _r_operation(self, left: FloatConvertible, ops: str) -> 'Float':
        target = Float._type_reduction(left)
        temp = Float._operate(target, self, ops)
        return temp

    def _i_operation(self, other: FloatConvertible, ops: str) -> None:
        target = Float._type_reduction(other)
        self.move("cache.left")
        target.move("cache.right")
        if ops == '+' or ops == '-':
            branch = 'plus' if ops == '+' else 'sub'
            Function(
                MCF.builtinSign(f"math.float.compute.run_{branch}")
            ).call()
            self.collect("register")
        elif ops == '*' or ops == '/':
            branch = 'mul' if ops == '*' else 'div'
            Function(
                MCF.builtinSign(f"math.float.compute.run_{branch}")
            ).call()
            self.collect("register")
        else:
            raise MCFTypeError(
                "Unsupported operation type '{}' for Float.", ops
            )

    def __add__(self, other: FloatConvertible) -> 'Float':
        try:
            return self._operation(other, '+')
        except MCFTypeError:
            return NotImplemented

    def __radd__(self, left: FloatConvertible) -> 'Float':
        try:
            return self._r_operation(left, '+')
        except MCFTypeError:
            return NotImplemented

    def __sub__(self, other: FloatConvertible) -> 'Float':
        try:
            return self._operation(other, '-')
        except MCFTypeError:
            return NotImplemented

    def __rsub__(self, left: FloatConvertible) -> 'Float':
        try:
            return self._r_operation(left, '-')
        except MCFTypeError:
            return NotImplemented
    
    def __mul__(self, other: FloatConvertible) -> 'Float':
        try:
            return self._operation(other, '*')
        except MCFTypeError:
            return NotImplemented
    
    def __rmul__(self, left: FloatConvertible) -> 'Float':
        try:
            return self._r_operation(left, '*')
        except MCFTypeError:
            return NotImplemented

    def __truediv__(self, other: FloatConvertible) -> 'Float':
        try:
            return self._operation(other, '/')
        except MCFTypeError:
            return NotImplemented
    
    def __rtruediv__(self, left: FloatConvertible) -> 'Float':
        try:
            return self._r_operation(left, '/')
        except MCFTypeError:
            return NotImplemented
    
    def __iadd__(self, other: FloatConvertible) -> 'Float':
        try:
            self._i_operation(other, '+')
        except MCFTypeError:
            return NotImplemented
        return self

    def __isub__(self, other: FloatConvertible) -> 'Float':
        try:
            self._i_operation(other, '-')
        except MCFTypeError:
            return NotImplemented
        return self
    
    def __imul__(self, other: FloatConvertible) -> 'Float':
        try:
            self._i_operation(other, '*')
        except MCFTypeError:
            return NotImplemented
        return self

    def __itruediv__(self, other: FloatConvertible) -> 'Float':
        try:
            self._i_operation(other, '/')
        except MCFTypeError:
            return NotImplemented
        return self


    def _compare(self, other: FloatConvertible, _type: str) -> Condition:
        result = Condition(False, False)
        other = Float._type_reduction(other)
        self.move("cache.left")
        other.move("cache.right")
        Function(MCF.builtinSign('math.float.compare.run')).call()
        if _type == '>':
            Execute().condition('if').score_matches(
                MCF.GENERAL, MCF.sb_sys, 1, 1
            ).run(
                ScoreBoard.players_set(result._mcf_id, MCF.sb_general, 1)
            )
        elif _type == '>=':
            Execute().condition('if').score_matches(
                MCF.GENERAL, MCF.sb_sys, 0, None
            ).run(
                ScoreBoard.players_set(result._mcf_id, MCF.sb_general, 1)
            )
        elif _type == '=':
            Execute().condition('if').score_matches(
                MCF.GENERAL, MCF.sb_sys, 0, 0
            ).run(
                ScoreBoard.players_set(result._mcf_id, MCF.sb_general, 1)
            )
        elif _type == '<':
            Execute().condition('if').score_matches(
                MCF.GENERAL, MCF.sb_sys, -1, -1
            ).run(
                ScoreBoard.players_set(result._mcf_id, MCF.sb_general, 1)
            )
        elif _type == '<=':
            Execute().condition('if').score_matches(
                MCF.GENERAL, MCF.sb_sys, None, 0
            ).run(
                ScoreBoard.players_set(result._mcf_id, MCF.sb_general, 1)
            )
        elif _type == '!=':
            Execute().condition('unless').score_matches(
                MCF.GENERAL, MCF.sb_sys, 0, 0
            ).run(
                ScoreBoard.players_set(result._mcf_id, MCF.sb_general, 1)
            )
        else:
            raise MCFTypeError(
                "Unsupported comparison type '{}' for Float.", _type
            )
        return result
        
    def __eq__(self, value: FloatConvertible) -> Condition:
        try:
            return self._compare(value, '=')
        except MCFTypeError:
            return NotImplemented
    
    def __ne__(self, value: FloatConvertible) -> Condition:
        try:
            return self._compare(value, '!=')
        except MCFTypeError:
            return NotImplemented
    
    def __lt__(self, value: FloatConvertible) -> Condition:
        try:
            return self._compare(value, '<')
        except MCFTypeError:
            return NotImplemented
    
    def __gt__(self, value: FloatConvertible) -> Condition:
        try:
            return self._compare(value, '>')
        except MCFTypeError:
            return NotImplemented

    def __ge__(self, value: FloatConvertible) -> Condition:
        try:
            return self._compare(value, '>=')
        except MCFTypeError:
            return NotImplemented
    
    def __le__(self, value: FloatConvertible) -> Condition:
        try:
            return self._compare(value, '<=')
        except MCFTypeError:
            return NotImplemented

    def rm(self):
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")


# ArrayList Implementation

ElementType = TypeVar("ElementType")
class _IterationContext(Generic[ElementType]):
    _iter_used: bool
    _control_sig: str
    _control_path: str
    _main_sig: str
    _main_path: str
    _index_id: str
    _iter_src: str
    _source: 'ArrayList[ElementType]'
    _ret_value: ElementType
    def __init__(
        self,
        src: 'ArrayList[ElementType]',
        element_type: type[ElementType]
    ):
        self._ret_value = element_type(init_val=None, void=False)
        self._iter_used = False
        self._control_path, self._control_sig = MCF.makeFunction()
        self._main_path, self._main_sig = MCF.makeFunction()
        self._iter_src = src._mcf_id
        self._source = src
        self._index_id = MCF.getFID()
        self._enter()
    
    def _enter(self) -> None:
        # save loop stack
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
        ScoreBoard.players_set(self._index_id, MCF.sb_general, 0)
        Function(self._control_sig).call()
        MCF.forward(self._control_path)
        # write control
        Execute().condition('if').score_matches(
            MCF.LOOP_EXIT, MCF.sb_sys, 1, 1
        ).run(
            ReturN().value(0)
        )
        ScoreBoard.players_set(MCF.LOOP_CONT, MCF.sb_sys, 0)
        Data.storage(MCF.storage).modify_set("call.m0").value(f'"{self._iter_src}"')
        Execute().store('result').storage(MCF.storage, "call.m1", 'int', 1.0).run(
            ScoreBoard.players_get(self._index_id, MCF.sb_general)
        )
        # validate
        Function(MCF.builtinSign('array_list.iterate')).with_args(
            Data.storage(MCF.storage), "call"
        )
        # return if out of range
        Execute().condition('if').score_matches(
            MCF.GENERAL, MCF.sb_sys, 0, 0
        ).run(
            ReturN().value(0)
        )
        # collect
        self._ret_value.collect("register")
        # call main
        Function(self._main_sig).call()
        MCF.forward(self._main_path)
        MCF._context_type.append('loop')
        MCF._last_ctx_type = 'norm'
    
    def __next__(self) -> ElementType:
        if self._iter_used:
            # leave
            MCF.rewind()
            ScoreBoard.players_add(self._index_id, MCF.sb_general, 1)
            Function(self._control_sig).call()
            MCF._last_ctx_type = MCF._context_type.pop()
            MCF.rewind()
            if MCF.do_gc:
                # gc iterator
                ScoreBoard.players_reset(self._index_id, MCF.sb_general)
                # delete ref from context
                self._ret_value.rm()
                MCF.removeContext(self._ret_value)
                self._ret_value._gc_sign = 'shadow'
            raise StopIteration
        self._iter_used = True
        return self._ret_value

Long = Annotated[Integer, 'long']
Int = Annotated[Integer, 'int']
Byte = Annotated[Integer, 'byte']

class ArrayList(Generic[ElementType], MCFVariable):
    _array_sign: ClassVar[dict[str, str]]
    _array_suffix: ClassVar[dict[str, str]]
    _raw_type: type
    _element_tp: type[MCFVariable] | None
    _arr_type: str

    def __init__(
        self,
        tp: type[ElementType] | None = None, 
        init_val: 'Iterable[ElementType] | ArrayList[ElementType] | None' = [],
        void: bool = False
    ):
        MCF.useComponent('array_list', built_cps.array_list)
        self._raw_type = tp
        if tp is None:
            self._element_tp = None
            self._arr_type = 'list'
        elif get_origin(tp) is Annotated:
            self._element_tp, self._arr_type = get_args(tp)
            if self._element_tp is not Integer:
                console.error(
                    MCFSyntaxError(
                        "ArrayList only accepts Annotated on Integer, not"
                        f" {self._element_tp}."
                    )
                )
                self._element_tp = Integer
            if self._arr_type not in self._array_sign.keys():
                console.error(
                    MCFSyntaxError(
                        "Annotated meta for Integer can only be one of "
                        f"{tuple(self._array_sign.keys())}."
                    )
                )
                self._arr_type = 'list'
        else:
            self._element_tp = tp
            self._arr_type = 'list'
            if not issubclass(tp, MCFVariable):
                console.error(
                    MCFTypeError(
                        "Element type for ArrayList must be a subclass of "
                        f"MCFVariable, not {tp}."
                    )
                )
                self._element_tp = None
        super().__init__(init_val, void)
    
    def assign(self, value: Iterable[ElementType] | 'ArrayList[ElementType]') -> None:
        if self._element_tp is None: return
        if isinstance(value, ArrayList):
            if value._element_tp is not self._element_tp:
                console.error(
                    MCFTypeError(
                        f"Arrays assigned should have same element type,"
                        f" while one is {self._element_tp},"
                        f" the other is {value._element_tp}."
                    )
                )
                return
            if value._arr_type != self._arr_type:
                console.error(
                    MCFTypeError(
                        f"Arrays assigned should have same array type,"
                        f" while one is {self._arr_type},"
                        f" the other is {value._arr_type}."
                    )
                )
                return
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
                Data.storage(MCF.storage), f"mem.{value._mcf_id}"
            )
        elif iterable(value):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(
                f"[{self._array_sign.get(self._arr_type, '')}]"
            )
            for element in value:
                if not isinstance(element, self._element_tp):
                    console.error(
                        MCFTypeError(
                            f"Element in iterable is of type {type(element)}"
                            f", while array requires type {self._element_tp}."
                        )
                    )
                    break
                if self._arr_type != 'list':
                    element: Integer
                    element.extract("register", self._arr_type)
                else:
                    element.move("register")
                Data.storage(MCF.storage).modify_append(
                    f"mem.{self._mcf_id}"
                ).via(
                    Data.storage(MCF.storage), "register"
                )
        else:
            console.error(
                MCFTypeError(
                    f"Value of type {type(value)} can't be assigned to an ArrayList."
                )
            )
    
    def move(self, dist: str) -> None:
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )

    def duplicate(
        self,
        init_val: 'Iterable[ElementType] | ArrayList[ElementType] | None' = [],
        void: bool = False
    ) -> 'ArrayList[ElementType]':
        return ArrayList(self._raw_type, init_val, void)
    
    def collect(self, src: str) -> None:
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), src
        )

    def extract(self, dist: str) -> None:
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )

    def construct(self, src: str) -> None:
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), src
        )

    def macro_construct(
        self,
        slot: str,
        mcf_id: str
    ) -> 'ArrayList[ElementType]':
        temp = ArrayList(self._raw_type, None, True)
        Data.storage(MCF.storage).modify_set(f"mem.{mcf_id}", True).via(
            Data.storage(MCF.storage), f"mem.$({slot})"
        )
        temp._mcf_id = mcf_id
        return temp

    def rm(self):
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")


    def size(self) -> Integer:
        if self._element_tp is None:
            raise NotImplementedError(
                "Method 'size' of ArrayList[None] is not defined."
            )
        ret = Integer(None, False)
        Execute().store('result').score(ret._mcf_id, MCF.sb_general).run(
            Data.storage(MCF.storage).get(f"mem.{self._mcf_id}")
        )
        return ret

    def append(self, element: ElementType) -> None:
        # invalid type
        if self._element_tp is None:
            raise NotImplementedError(
                "Method 'append' of ArrayList[None] is not defined."
            )
        # not the same type
        if type(element) is not self._element_tp:
            console.error(
                MCFTypeError(
                    f"ArrayList here requires type {self._element_tp}."
                )
            )
            return
        element.move("register")
        Data.storage(MCF.storage).modify_append(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), "register"
        )

    def insert(
        self,
        index: IntegerConvertible,
        element: ElementType
    ) -> None:
        if self._element_tp is None:
            raise NotImplementedError(
                "Method 'insert' of ArrayList[None] is not defined."
            )
        if type(element) is not self._element_tp:
            console.error(
                MCFTypeError(
                    f"ArrayList requires type {self._element_tp}."
                )
            )
            return
        # store index
        if isinstance(index, int):
            Data.storage(MCF.storage).modify_set("call.m0").value(str(index))
        elif isinstance(index, Integer):
            index.move("call.m0")
        else:
            console.error(
                MCFTypeError(
                    f"Invalid index type: {type(index)}."
                )
            )
        # save list ptr
        Data.storage(MCF.storage).modify_set("call.m1").value(f'"{self._mcf_id}"')
        # move element to register
        element.move("register")
        # call
        Function(MCF.builtinSign('array_list.insert')).with_args(
            Data.storage(MCF.storage), "call"
        )

    def prepend(self, element: ElementType) -> None:
        # invalid type
        if self._element_tp is None:
            raise NotImplementedError(
                "Method 'prepend' of ArrayList[None] is not defined."
            )
        # not the same type
        if type(element) is not self._element_tp:
            console.error(
                MCFTypeError(
                    f"ArrayList here requires type {self._element_tp}."
                )
            )
            return
        element.move("register")
        Data.storage(MCF.storage).modify_prepend(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), "register"
        )

    def pop(self, index: IntegerConvertible = -1) -> ElementType:
        """Pop last element by default."""
        if self._element_tp is None:
            raise NotImplementedError(
                "Method 'pop' of ArrayList[None] is not defined."
            )
        # export index on m0
        if isinstance(index, int):
            Data.storage(MCF.storage).modify_set("call.m0").value(str(index))
        elif isinstance(index, Integer):
            index.move("call.m0")
        else:
            console.error(
                MCFTypeError(
                    f"Invalid index type: {type(index)}."
                )
            )
        # store list ptr
        Data.storage(MCF.storage).modify_set("call.m1").value(f'"{self._mcf_id}"')
        Function(MCF.builtinSign('array_list.pop')).with_args(
            Data.storage(MCF.storage), "call"
        )
        # create return value
        ret_value = self._element_tp(init_val=None, void=False)
        ret_value.collect("register")
        return ret_value
    
    def extend(self, src: 'ArrayList[ElementType]') -> None:
        src.move("cache.src")
        self.move("register")
        Function(MCF.builtinSign('array_list.extend')).call()
        self.collect("register")
    
    def __add__(self, src: 'ArrayList[ElementType]') -> 'ArrayList[ElementType]':
        temp = ArrayList(self._raw_type, self)
        temp.extend(src)
        return temp

    def __iadd__(self, src: 'ArrayList[ElementType]') -> 'ArrayList[ElementType]':
        self.extend(src)
        return self

    @overload
    def __getitem__(self, index: IntegerConvertible) -> ElementType: ...

    @overload
    def __getitem__(self, _slice: slice) -> 'ArrayList[ElementType]': ...

    def __getitem__(
        self,
        index_or_slice: 'IntegerConvertible | slice'
    ) -> 'ElementType | ArrayList[ElementType]':
        if self._element_tp is None:
            raise NotImplementedError(
                "Method '__getitem__' of ArrayList[None] is not defined."
            )
        if isinstance(index_or_slice, int):
            Data.storage(MCF.storage).modify_set("call.m0").value(str(index_or_slice))
            Data.storage(MCF.storage).modify_set("call.m1").value(f'"{self._mcf_id}"')
            Function(MCF.builtinSign('array_list.at')).with_args(
                Data.storage(MCF.storage), "call"
            )
            ret_val = self._element_tp(init_val=None, void=False)
            ret_val.collect("register")
            return ret_val
        elif isinstance(index_or_slice, Integer):
            index_or_slice.move("call.m0")
            Data.storage(MCF.storage).modify_set("call.m1").value(f'"{self._mcf_id}"')
            Function(MCF.builtinSign('array_list.at')).with_args(
                Data.storage(MCF.storage), "call"
            )
            ret_val = self._element_tp(init_val=None, void=False)
            ret_val.collect("register")
            return ret_val
        elif isinstance(index_or_slice, slice):
            # validate args
            def validate_args(
                arg: 'IntegerConvertible | None',
                name: str
            ) -> None:
                if arg is None: return
                if not isinstance(arg, int) and not isinstance(arg, Integer):
                    console.error(
                        MCFTypeError(
                            f"{name} of slice for ArrayList must be of type "
                            f"int or Integer, not {type(arg)}."
                        )
                    )
            validate_args(index_or_slice.start, 'Start')
            validate_args(index_or_slice.stop, 'Stop')
            validate_args(index_or_slice.step, 'Step')
            # optional reduction
            def move_score(arg: IntegerConvertible, place: str) -> None:
                if isinstance(arg, Integer):
                    ScoreBoard.players_operation(
                        place, MCF.sb_sys, "=",
                        arg._mcf_id, MCF.sb_general
                    )
                else:
                    ScoreBoard.players_set(place, MCF.sb_sys, arg)
            if index_or_slice.start is None:
                ScoreBoard.players_set(MCF.BUFFER1, MCF.sb_sys, 0)
            else:
                move_score(index_or_slice.start, MCF.BUFFER1)
            if index_or_slice.stop is None:
                Execute().store('result').score(MCF.BUFFER2, MCF.sb_sys).run(
                    Data.storage(MCF.storage).get(f"mem.{self._mcf_id}")
                )
            else:
                move_score(index_or_slice.stop, MCF.BUFFER2)
            if index_or_slice.step is None:
                ScoreBoard.players_set(MCF.BUFFER3, MCF.sb_sys, 1)
            else:
                move_score(index_or_slice.step, MCF.BUFFER3)
            # both None swap
            if index_or_slice.start is None and index_or_slice.stop is None:
                Execute().condition('if').score_matches(
                    MCF.BUFFER3, MCF.sb_sys, None, -1
                ).run(
                    Function(MCF.builtinSign('array_list.swap')).call()
                )
            # run component
            self.move("cache.src")
            Data.storage(MCF.storage).modify_set("register").value(
                f"[{self._array_sign.get(self._arr_type, '')}]"
            )
            Function(MCF.builtinSign('array_list.slice')).call()
            # collect ret_val
            ret_val = ArrayList(self._raw_type, None, False)
            ret_val.collect("register")
            return ret_val
        else:
            console.error(
                MCFTypeError(
                    f"Invalid argument for get item operation: {index_or_slice},"
                    "argument must be an IntegerConvertible or a slice."
                )
            )

    def __iter__(self) -> _IterationContext[ElementType]:
        if self._element_tp is None:
            raise NotImplementedError(
                "Method '__iter__' of ArrayList[None] is not defined."
            )
        return _IterationContext(self, self._element_tp)

ArrayList._array_sign = {
    'byte': 'B;',
    'int': 'I;',
    'long': 'L;'
}
ArrayList._array_suffix = {
    'byte': 'b',
    'long': 'l'
}


# String Implementation -> Text

TextConvertible: TypeAlias = 'Text | str'
class Text(MCFVariable):
    def __init__(
        self,
        init_val: Optional[TextConvertible] = "",
        void: bool = False
    ):
        MCF.useComponent('string', built_cps.string)
        super().__init__(init_val, void)
    
    def assign(self, value: TextConvertible) -> None:
        if isinstance(value, str):
            value = value.replace('"', r'\"')
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(
                f'"{value}"'
            )
        elif isinstance(value, Text):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
                Data.storage(MCF.storage), f"mem.{value._mcf_id}"
            )
        else:
            console.error(
                MCFTypeError(
                    f"Can not assign variable of type {type(value)} to a Text."
                )
            )

    def move(self, dist: str) -> None:
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )

    def collect(self, src: str) -> None:
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), src
        )

    def extract(self, dist: str) -> None:
        self.move(dist)

    def construct(self, src: str):
        self.collect(src)

    @staticmethod
    def duplicate(
        init_val: Optional[TextConvertible] = '',
        void: bool = False
    ) -> 'Text':
        return Text(init_val=init_val, void=void)

    def rm(self) -> None:
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")

    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> 'Text':
        temp = Text(None, True)
        temp._mcf_id = mcf_id
        Data.storage(MCF.storage).modify_set(f"mem.{temp._mcf_id}", True).via(
            Data.storage(MCF.storage), f"mem.$({slot})"
        )
        return temp


    def substr(
        self,
        start: Optional[IntegerConvertible] = None,
        end: Optional[IntegerConvertible] = None  
    ) -> 'Text':            
        def validate(arg: IntegerConvertible):
            if not isinstance(arg, int) and not isinstance(arg, Integer):
                console.error(
                    MCFTypeError(
                        "Argument for Text.substr should be a Text or str,"
                        f" not {type(arg)}."
                    )
                )
        if start is None:
            Data.storage(MCF.storage).modify_set("call.m1").value("0")
        else:
            validate(start)
            if isinstance(start, int):
                Data.storage(MCF.storage).modify_set("call.m1").value(str(start))
            else:
                start.move("call.m1")
        if end is None:
            Execute().store('result').storage(
                MCF.storage, "call.m2", 'int', 1.0
            ).run(
                Data.storage(MCF.storage).get(f"mem.{self._mcf_id}")
            )
        else:
            validate(end)
            if isinstance(end, int):
                Data.storage(MCF.storage).modify_set("call.m2").value(str(end))
            else:
                end.move("call.m2")
        Data.storage(MCF.storage).modify_set("call.m0").value(f'"{self._mcf_id}"')
        Function(MCF.builtinSign('string.sub_text')).with_args(
            Data.storage(MCF.storage), "call"
        )
        ret_val = Text(None, False)
        ret_val.collect("register")
        return ret_val

    def size(self) -> Integer:
        ret_ = Integer(None, False)
        Execute().store('result').score(ret_._mcf_id, MCF.sb_general).run(
            Data.storage(MCF.storage).get(f"mem.{self._mcf_id}")
        )
        return ret_

    def push_back(self, text: TextConvertible) -> None:
        if isinstance(text, str):
            text = text.replace('"', r'\"')
            Data.storage(MCF.storage).modify_set("call.m1").value(f'"{text}"')
        elif isinstance(text, Text):
            text.move("call.m1")
            Execute().condition('if').data(
                Data.storage(MCF.storage), 'call{m1:"\'"}'
            ).run(
                Data.storage(MCF.storage).modify_set("call.m1").value(
                    '"\\\\\'"'
                )
            )
        else:
            console.error(
                MCFTypeError(
                    "Argument for Text.push should be a Text or str, "
                    f"not {type(text)}."
                )
            )
        self.move("call.m0")
        Function(MCF.builtinSign('string.combine')).with_args(
            Data.storage(MCF.storage), "call"
        )
        self.collect("register")

    def __ne__(self, text: TextConvertible) -> Condition:
        result = Condition(None, False)
        self.move("register")
        if isinstance(text, str):
            text = text.replace('"', r'\"')
            Data.storage(MCF.storage).modify_set("cache.src").value(
                f'"{text}"'
            )
        elif isinstance(text, Text):
            text.move("cache.src")
        else:
            console.error(
                MCFTypeError(
                    "Argument for Text.__eq__ should be a Text or str, "
                    f"not {type(text)}."
                )
            )
        Execute().store('success').score(MCF.GENERAL, MCF.sb_sys).run(
            Data.storage(MCF.storage).modify_set("register").via(
                Data.storage(MCF.storage), "cache.src"
            )
        )        
        ScoreBoard.players_operation(
            result._mcf_id, MCF.sb_general, "=",
            MCF.GENERAL, MCF.sb_sys
        )
        return result

    def __eq__(self, text: TextConvertible) -> Condition:
        result = self.__ne__(text)
        result.Reverse()
        return result
