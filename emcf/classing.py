
from .types import *
from ._writers import *
from ._utils import console
from .functional import push_stack, new_stack, pop_stack
from .display import say
from .core import MCF, MCFCore
from ._exceptions import MCFSyntaxError, MCFValueError, MCFTypeError
from typing import Type, Self, TypeVarTuple, TypeVar, Any, NewType, Callable
from functools import wraps

__all__ = [
    'MCFClass',
    'IgnoredMethod'
]

class MetaInfo:
    cls: Type
    cls_name: str
    name_type_map: dict[str, Type]
    name_id_map: dict[str, str]
    name_shadow_map: dict[str, MCFVariable]
    exported_map: dict[str, dict[str, MCFVariable]]
    init_detail: tuple[str, str]

    def __init__(
        self,
        cl: Type,
        cn: str,
        ntm: dict[str, Type],
        nim: dict[str, str],
    ):
        self.cls = cl
        self.cls_name = cn
        self.name_type_map = ntm
        self.name_id_map = nim
        self.init_detail = MCF.makeFunction()
        self.exported_map = {}


resolution_cache: dict[str, MetaInfo] = {}
method_ignored: set[str] = set()

Mtd = TypeVar("Method")
def IgnoredMethod(target: Mtd) -> Mtd:
    method_ignored.add(f"{target.__module__}[{target.__qualname__}]")
    return target

# method do not support Ref at present
# init arguments can not be used in __init__ context
# __init__ function should be strictly formatted

Ret = TypeVar("ReturnType")
Args = TypeVarTuple("Args")
class MCFClass(MCFVariable):
    """MCF的类支持，继承自MCFVariable"""
    _meta: MetaInfo

    def __init__(
        self,
        cls: Type,
        kws: dict[str, Any],
        **kwargs: MCFVariable
    ):
        """初始化一个自定义类。"""
        void = kws.get("void", False)
        super().__init__(None, void)
        # empty cls
        if cls is None: return
        first_init = True

        def create_meta():
            nonlocal first_init
            # resolution
            meta = resolution_cache.get(cls.__name__, None)
            if meta is not None:
                first_init = False
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

            self._meta = MetaInfo(cls, cls.__name__, cls_info, fid_map)
            resolution_cache[cls.__name__] = self._meta

        def open_mem():
            self._meta.name_shadow_map = {}
            for name, tp in self._meta.name_type_map.items():
                fid = self._meta.name_id_map[name]
                value: MCFVariable = tp(init_val=None, void=True)
                value._mcf_id = fid
                value._gc_sign = 'shadow'
                value._meta = 'cls'
                self._meta.name_shadow_map[name] = value

        def decorate(
            method: Callable[[*Args], Ret],
            cls_meta: MetaInfo,
            func_detail: tuple[str, str],
            body_detail: tuple[str, str]
        ) -> Callable[[*Args], Ret]:
            static = isinstance(method, staticmethod)
            if static:
                arg_count = method.__func__.__code__.co_argcount
            else:
                arg_count = method.__code__.co_argcount
            mcf_id = self._mcf_id
            ret_tp = method.__annotations__.get("return", None)
            if ret_tp is None:
                console.error(
                    MCFSyntaxError(
                        f"Need a return type annotation for method"
                        f" {method.__name__} in class {cls_meta.cls_name}."
                    )
                )
                return method
            if type(ret_tp) is not type:
                if ret_tp == cls_meta.cls_name:
                    ret_tp = cls
                else:
                    console.error(
                        MCFTypeError(
                            f'Return annotation (at method {method.__name__}, '
                            f'in class {cls_meta.cls_name}) is not a class '
                            'but "{}".',
                            ret_tp
                        )
                    )
                    return method
            if not issubclass(ret_tp, MCFVariable):
                console.error(
                    MCFTypeError(
                        'Return type "{}" (at method '
                        f'{method.__name__}, in class {cls_meta.cls_name})'
                        ' is not a subclass of MCFVariable.',
                        ret_tp
                    )
                )
                return method

            @wraps(method)
            def wrapper(*args: *Args) -> Ret:
                start = 0 if static else 1
                arg_check = True
                if len(args) > arg_count:
                    console.error(
                        MCFValueError(
                            f"Method {method.__qualname__} requires "
                            f"{arg_count} arguments while {len(args)} are given."
                        )
                    )
                    arg_check = False
                for index in range(start, len(args)):
                    if not isinstance(args[index], MCFVariable):
                        console.error(
                            MCFTypeError(
                                'Parameter of type "{}" can not be passed in '
                                'a MCF method context.', type(args[index])
                            )
                        )
                        arg_check = False
                if not arg_check:
                    ret_val = ret_tp(init_val=None, void=True)
                    ret_val._gc_sign = 'shadow'
                    return ret_val

                # save present context
                push_stack()

                # collect self data
                if not static:
                    for _, shadow in cls_meta.name_shadow_map.items():
                        shadow.collect(f"mem.{mcf_id}.{shadow._mcf_id}")

                # export parameters
                for index in range(start, len(args)):
                    Data.storage(MCF.storage).modify_set(
                        f"call.m{index}"
                    ).value(
                        f'"{args[index]._mcf_id}"'
                    )

                # check if method is not exported
                export_info = cls_meta.exported_map.get(method.__name__, None)
                if export_info is None:
                    export_info = {}
                    cls_meta.exported_map[method.__name__] = export_info
                    # forward to entry
                    MCF.forward(func_detail[0])
                    # do exportation on args
                    collected = []
                    if not static: collected.append(args[0])
                    for index in range(start, len(args)):
                        new: MCFVariable = args[index].macro_construct(
                            f"m{index}", MCF.getFID()
                        )
                        new._gc_sign = 'shadow'
                        export_info[new._mcf_id] = new
                        collected.append(new)
                    # add context of self
                    if not static:
                        export_info.update(self._meta.name_shadow_map)
                    # update context & call
                    MCF._context.update(export_info)
                    new_stack()
                    Function(body_detail[1]).call()
                    # forward to body
                    MCF.forward(body_detail[0])
                    method(*collected)
                    MCF.rewind()

                    # gc
                    if MCF.do_gc:
                        for index in range(start, len(args)):
                            collected[index].rm()
                    MCF.rewind()
                else:
                    MCF._context.update(export_info)
                    new_stack()
                
                # call function
                Function(func_detail[1]).with_args(
                    Data.storage(MCF.storage), "call"
                )
                
                # recover context
                pop_stack()

                # collect return value
                if issubclass(ret_tp, FakeNone):
                    ret_val = None
                else:
                    ret_val = ret_tp(init_val=None, void=False)
                    ret_val.collect("ret_val")
                    MCF.addContext(ret_val)

                # store members back to class
                if not static:
                    for shadow in cls_meta.name_shadow_map.values():
                        shadow.move(f"mem.{mcf_id}.{shadow._mcf_id}")

                return ret_val
            
            wrapper.__mcfsignature__ = func_detail[1]
            if static: return staticmethod(wrapper)
            else: return wrapper

        def resolve_method():
            for name, method in cls.__dict__.items():
                if name.startswith('__') or name.endswith('__'):
                    continue
                if not callable(method):
                    continue
                func_id = f"{method.__module__}[{method.__qualname__}]"
                if func_id in method_ignored:
                    console.warn(
                        f"""Method {func_id} explicitly ignored."""
                    )
                    continue
                setattr(
                    cls, name,
                    decorate(
                        method, self._meta,
                        MCF.makeFunction(), MCF.makeFunction()
                    )
                )

        create_meta()
        if first_init:
            open_mem()
            resolve_method()
        if void:
            return

        self.temp = []
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(r"{}")
        for name, shadow in self._meta.name_shadow_map.items():
            init = kwargs.get(name, None)
            if init is None:
                console.error(
                    MCFValueError(
                        f"Member {name} in class {self._meta.cls_name} is not"
                        " initialized."
                    )
                )
            else:
                self.temp.append(init)
                shadow.assign(init)
            setattr(self, name, shadow)
        
        # push frame
        push_stack()

        # add members to context
        new_stack()
        MCF._context.update(self._meta.name_shadow_map)

        # forward to init context
        MCF.forward(self._meta.init_detail[0])

    def complete(self) -> None:
        # rewind from init context
        MCF.rewind()
        # write init call
        Function(self._meta.init_detail[1]).call()
        # pop stack
        pop_stack()
        # clear init values
        del self.temp
        # save back to class
        for shadow in self._meta.name_shadow_map.values():
            shadow.move(f"mem.{self._mcf_id}.{shadow._mcf_id}")


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

    def macro_construct(self, slot: str, mcf_id: str) -> Self:
        """默认宏构造函数"""
        temp = self._meta.cls(void=True)



    def duplicate(self, init_val: Any = None, void = False) -> Self:
        """产生MCFClass对象。

        注意：该方法并不能用于复制一个类的实例，该方法产生的实例仅保证MCFVariable的
        内部操作是可用的，不能保证编写的自定义类的方法同样可用。

        若需要复制一个自定义类，请在自定义类的`__init__`方法中做修改，使其支持复制
        操作。
        """
        return MCFClass(None, void)
    
    def rm(self):
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")
