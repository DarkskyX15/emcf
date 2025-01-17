
from .types import *
from ._utils import console
from ._writers import *
from .core import MCF
from ._exceptions import MCFSyntaxError
from typing import Type, Self, Generic, TypeVar, Any

Ret = TypeVar("ReturnValue")
class MCFMethod(Generic[Ret]):
    pass

class MetaInfo:
    cls_name: str
    name_type_map: dict[str, Type]
    name_id_map: dict[str, str]

    def __init__(
        self,
        cn: str,
        ntm: dict[str, Type],
        nim: dict[str, str],
    ):
        self.cls_name = cn
        self.name_type_map = ntm
        self.name_id_map = nim

resolution_cache: dict[str, MetaInfo] = {}

class MCFClass(MCFVariable):
    """MCF的类支持，继承自MCFVariable"""
    _meta: MetaInfo

    def __init__(
        self,
        cls: Type,
        init_val: None = None,
        void: bool = False
    ):
        """初始化一个自定义类。"""
        super().__init__(init_val, void)

        def create_meta():
            # process cls data
            if cls is None: return
            # resolution
            meta = resolution_cache.get(cls.__name__, None)
            if meta is not None:
                self._meta = meta
                return
            cls_info = {}
            # resolve cls
            for name, tp in cls.__annotations__.items():
                if type(tp) is type and issubclass(tp, MCFVariable):
                    cls_info[name] = tp
                    continue
                if isinstance(tp, object):
                    if isinstance(tp, str):
                        if tp == cls.__name__:
                            cls_info[name] = cls
                            continue
                    console.warn(
                        f"{name}: {tp} (in module {cls.__module__}, class {cls.__name__})"
                        " is not a valid MCFClass annotation in this context."
                    )
            # fid_map
            fid_map = {}
            for name in cls_info.keys():
                fid_map[name] = MCF.getFID()

            self._meta = MetaInfo(cls.__name__, cls_info, fid_map)
            resolution_cache[cls.__name__] = self._meta


        create_meta()

    def assign(self, value: Self) -> None:
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), f"mem.{value._mcf_id}"
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
        """派生类应该自行实现解包操作"""
        raise NotImplementedError

    def construct(self, src: str) -> None:
        """派生类应该自行实现构造函数"""
        raise NotImplementedError

    def inplace_construct(self, src: str) -> None:
        pass

    @staticmethod
    def macro_construct(slot: str, mcf_id: str):
        """派生类应该自行实现宏构造函数"""
        raise NotImplementedError

    def duplicate(self, init_val = None, void = False) -> Self:
        """产生与自身类型相同的对象。

        注意：该方法并不能用于复制一个类的实例，该方法产生的实例仅保证MCFVariable的
        内部操作是可用的，不能保证编写的自定义类的方法同样可用。

        若需要复制一个自定义类，请在自定义类的`__init__`方法中做修改，使其支持复制
        操作。
        """
        return MCFClass(None, init_val, void)
    
    def rm(self):
        pass

class Array(MCFClass):
    size: 'Array'
    tem: Integer
    def __init__(self):
        self.arr = []

        super().__init__(Array)
        
    
    def wake():
        pass

