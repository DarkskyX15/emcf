"""
MCF所有基础变量的封装
"""

from .core import MCF, GCSign
from ._utils import console
from ._exceptions import *
from ._writers import *
from ._components import builtin_components as built_cps
from typing import TypeAlias, NewType, Any, Union, TextIO, Self, Literal


__all__ = [
    'MCFVariable',
    'FakeNone',
    'Condition',
    'Integer',
    'Float',
]


class MCFVariable:
    """MCF变量的基类

    所有的内置MCF变量都需要直接继承自`MCFVariable`
    """
    _mcf_id: str
    _gc_sign: GCSign
    _meta: str

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
        self._meta = 'norm'
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
    def macro_construct(slot: str, mcf_id: str) -> Self:
        """从`slot`指定的宏位置创建Fool ID为`mcf_id`的实例"""
        raise NotImplementedError

    @staticmethod
    def duplicate(
        init_val: Any = None,
        void: bool = False
    ) -> Self:
        """产生与自身类型相同的对象"""
        raise NotImplementedError

    def rm(self):
        """写清除指令，但不将自身移出上下文"""
        raise NotImplementedError


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
    ) -> Self:
        return FakeNone(None, True)

    # 不做回收处理
    def __del__(self):
        pass


Float = NewType("Float", MCFVariable)
FloatConvertible: TypeAlias = Float | float | int

Condition = NewType("Condition", MCFVariable)
ConditionConvertible: TypeAlias = Condition | bool

Integer = NewType("Integer", MCFVariable)
IntegerConvertible: TypeAlias = Integer | int


class Condition(MCFVariable):
    """布尔值类型"""
    def __init__(
        self,
        init_val: ConditionConvertible | None = False,
        void: bool = False
    ):
        super().__init__(init_val, void)

    def assign(self, value: ConditionConvertible) -> Condition:
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
    def macro_construct(slot: str, mcf_id: str) -> Condition:
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
        init_val: ConditionConvertible | None = False,
        void: bool = False
    ) -> Condition:
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

    def And(self, value: ConditionConvertible) -> Condition:
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

    def Or(self, value: ConditionConvertible) -> Condition:
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

    def Not(self) -> Condition:
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


class Integer(MCFVariable):

    def __init__(
        self,
        init_val: IntegerConvertible | Float | None = 0,
        void: bool = False
    ):
        super().__init__(init_val, void)

    def assign(self, value: IntegerConvertible | Float) -> Integer:
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
        return self

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
    def macro_construct(slot: str, mcf_id: str) -> Integer:
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
        init_val: IntegerConvertible | None = 0,
        void: bool = False
    ) -> Integer:
        return Integer(init_val, void)

    def __pos__(self) -> Integer:
        return Integer(self)

    def __neg__(self) -> Integer:
        temp = Integer(self)
        ScoreBoard.players_set(MCF.CALC_CONST, MCF.sb_sys, -1)
        ScoreBoard.players_operation(
            temp._mcf_id, MCF.sb_general, "*=",
            MCF.CALC_CONST, MCF.sb_sys
        )
        return temp

    def __abs__(self) -> Integer:
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
    ) -> Integer:
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
    ) -> Integer:
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
            cmp_range = [None, None]
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


class Float(MCFVariable):
    def __init__(
        self,
        init_val: FloatConvertible | Integer | None = 0.0,
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

    def assign(self, value: FloatConvertible | Integer) -> Float:
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
        return self
    
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
        init_val: FloatConvertible | None = 0.0,
        void: bool = False
    ) -> Float:
        return Float(init_val, void)
    
    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> Float:
        temp = Float(None, True)
        temp._mcf_id = mcf_id
        Data.storage(MCF.storage).modify_set(f"mem.{mcf_id}", True).via(
            Data.storage(MCF.storage), f"mem.$({slot})"
        )
        return temp

    @staticmethod
    def _type_reduction(other: FloatConvertible) -> Float:
        reduced = float(other) if isinstance(other, int) else other
        if not isinstance(reduced, float) and not isinstance(reduced, Float):
            raise MCFTypeError("Can not operate {} with a Float.", other)
        reduced = Float(reduced) if isinstance(reduced, float) else reduced
        return reduced

    @staticmethod
    def _operate(left: Float, right: Float, ops: str) -> Float:
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

    def _operation(self, other: FloatConvertible, ops: str) -> Float:
        target = Float._type_reduction(other)
        temp = Float._operate(self, target, ops)
        return temp

    def _r_operation(self, left: FloatConvertible, ops: str) -> Float:
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

    def __add__(self, other: FloatConvertible) -> Float:
        try:
            return self._operation(other, '+')
        except MCFTypeError:
            return NotImplemented

    def __radd__(self, left: FloatConvertible) -> Float:
        try:
            return self._r_operation(left, '+')
        except MCFTypeError:
            return NotImplemented

    def __sub__(self, other: FloatConvertible) -> Float:
        try:
            return self._operation(other, '-')
        except MCFTypeError:
            return NotImplemented

    def __rsub__(self, left: FloatConvertible) -> Float:
        try:
            return self._r_operation(left, '-')
        except MCFTypeError:
            return NotImplemented
    
    def __mul__(self, other: FloatConvertible) -> Float:
        try:
            return self._operation(other, '*')
        except MCFTypeError:
            return NotImplemented
    
    def __rmul__(self, left: FloatConvertible) -> Float:
        try:
            return self._r_operation(left, '*')
        except MCFTypeError:
            return NotImplemented

    def __truediv__(self, other: FloatConvertible) -> Float:
        try:
            return self._operation(other, '/')
        except MCFTypeError:
            return NotImplemented
    
    def __rtruediv__(self, left: FloatConvertible) -> Float:
        try:
            return self._r_operation(left, '/')
        except MCFTypeError:
            return NotImplemented
    
    def __iadd__(self, other: FloatConvertible) -> Float:
        try:
            self._i_operation(other, '+')
        except MCFTypeError:
            return NotImplemented
        return self

    def __isub__(self, other: FloatConvertible) -> Float:
        try:
            self._i_operation(other, '-')
        except MCFTypeError:
            return NotImplemented
        return self
    
    def __imul__(self, other: FloatConvertible) -> Float:
        try:
            self._i_operation(other, '*')
        except MCFTypeError:
            return NotImplemented
        return self

    def __itruediv__(self, other: FloatConvertible) -> Float:
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
