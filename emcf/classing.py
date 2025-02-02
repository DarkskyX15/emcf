
from .types import *
from ._writers import *
from ._utils import console
from .functional import push_stack, new_stack, pop_stack
from .core import MCF
from ._exceptions import MCFSyntaxError, MCFValueError, MCFTypeError
from typing import ( 
    Type, Self, TypeVarTuple, TypeVar, Any, Callable, get_origin, get_args,
    Annotated
)
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
# __init__ function should be strictly formatted

Ret = TypeVar("ReturnType")
Args = TypeVarTuple("Args")
class MCFClass(MCFVariable):
    """MCF的类支持，继承自MCFVariable"""
    _meta: MetaInfo

    def __init__(
        self,
        cls: Type,
        args: tuple[MCFVariable],
        kwargs: dict[str, MCFVariable],
        constructor: Callable[..., None],
        **init_args: tuple
    ):
        """初始化一个自定义类。"""
        init_val = kwargs.pop("init_val", 'val')
        void = kwargs.pop("void", False)

        def create_meta(out_self: 'MCFClass', cls):
            # resolution
            meta = resolution_cache.get(cls.__name__, None)
            if meta is not None:
                out_self._meta = meta
                return False
            cls_info = {}
            # resolve cls
            for name, tp in cls.__annotations__.items():
                origin = get_origin(tp)
                if origin is not None:
                    tp = origin
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

            resolution_cache[cls.__name__] = MetaInfo(
                cls, cls.__name__, cls_info, fid_map
            )
            out_self._meta = resolution_cache[cls.__name__]
            return True

        def open_mem(out_self: 'MCFClass'):
            out_self._meta.name_shadow_map = {}
            for name, tp in out_self._meta.name_type_map.items():
                args = init_args.get(name, ())
                fid = out_self._meta.name_id_map[name]
                value: MCFVariable = tp(*args, init_val=None, void=True)
                value._mcf_id = fid
                value._gc_sign = 'shadow'
                value._var_meta = 'cls'
                out_self._meta.name_shadow_map[name] = value

        def decorate(
            out_self: 'MCFClass',
            cls: Type,
            method: Callable[[*Args], Ret],
            func_detail: tuple[str, str],
            body_detail: tuple[str, str]
        ) -> Callable[[*Args], Ret]:
            cls_meta = out_self._meta
            static = isinstance(method, staticmethod)
            if static:
                arg_count = method.__func__.__code__.co_argcount
            else:
                arg_count = method.__code__.co_argcount
            ret_tp = method.__annotations__.get("return", None)
            extra_args = ()
            if ret_tp is None:
                console.error(
                    MCFSyntaxError(
                        f"Need a return type annotation for method"
                        f" {method.__name__} in class {cls_meta.cls_name}."
                    )
                )
                return method
            if type(ret_tp) is not type:
                origin = get_origin(ret_tp)
                if origin is not None:
                    if origin is Annotated:
                        ret_tp, extra_args = get_args(ret_tp)
                    else:
                        ret_tp = origin
                elif ret_tp == cls_meta.cls_name:
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
                mcf_id = args[0]._mcf_id if not static else 'ERR'
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
                    ret_val = ret_tp(*extra_args, init_val=None, void=True)
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
                        for value in cls_meta.name_shadow_map.values():
                            export_info[value._mcf_id] = value
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
                    ret_val = ret_tp(*extra_args, init_val=None, void=False)
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

        def resolve_init(
            out_self: 'MCFClass',
            func: Callable[..., None],
            args: list,
            kwargs: dict[str, Any]
        ):
            MCF.forward(out_self._meta.init_detail[0])
            index = 0
            new_args = []
            new_kwargs = {}
            for arg in args:
                new_arg = arg.macro_construct(f"m{index}", MCF.getFID())
                new_args.append(new_arg)
                MCF.addContext(new_arg)
                index += 1
            for name, kwarg in kwargs.items():
                new_kwarg = kwarg.macro_construct(f"m{index}", MCF.getFID())
                new_kwargs[name] = new_kwarg
                MCF.addContext(new_kwarg)
                index += 1
            # body info
            body_path, body_sig = MCF.makeFunction()
            # forward to body
            MCF.forward(body_path)
            func(*new_args, **new_kwargs)
            MCF.rewind()
            # call function
            Function(body_sig).call()

        def resolve_method(
            out_self: 'MCFClass',
            cls: Type,
            decorator: Callable 
        ):
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
                    decorator(
                        out_self, cls, method,
                        MCF.makeFunction(), MCF.makeFunction()
                    )
                )

        # init class meta
        first_init = create_meta(self, cls)
        if first_init:
            open_mem(self)

        # do not call assign on init
        super().__init__(None, void)

        if first_init:
            resolve_method(self, cls, decorate)

        # setup attributes
        for name, shadow in self._meta.name_shadow_map.items():
            setattr(self, name, shadow)

        # stop creating command if is an void value
        if void: return

        # create body
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(r"{}")
        
        # stop construct call if init_val is None
        if init_val is None: return

        # argument check
        cstr_count = constructor.__code__.co_argcount
        current_count = len(args) + len(kwargs)
        if current_count != cstr_count - 1:
            console.error(
                MCFValueError(
                    f"Constructor in class {self._meta.cls_name} needs"
                    f"{cstr_count - 1} arguments, while {current_count} are given."
                )
            )
            # do not construct if args do not match
            return
        
        # move arguments
        index = 0
        for arg in args:
            if not isinstance(arg, MCFVariable):
                console.error(
                    MCFTypeError(
                        "Cannot pass argument of type {} to constructor of "
                        f"class {self._meta.cls_name}.", type(arg)
                    )
                )
            Data.storage(MCF.storage).modify_set(f"call.m{index}").value(
                f'"{arg._mcf_id}"'
            )
            index += 1
        for name, arg in kwargs.items():
            if not isinstance(arg, MCFVariable):
                console.error(
                    MCFTypeError(
                        "Cannot pass keyword argument of type {} to"
                        f"constructor of class {self._meta.cls_name}.",
                        type(arg)
                    )
                )
            Data.storage(MCF.storage).modify_set(f"call.m{index}").value(
                f'"{arg._mcf_id}"'
            )
            index += 1

        # push frame to call construct
        push_stack()

        # add members to context
        new_stack()
        for shadow in self._meta.name_shadow_map.values():
            MCF._context[shadow._mcf_id] = shadow
        
        # write constructor if first init
        if first_init:
            resolve_init(self, constructor, args, kwargs)
            MCF.rewind()

        # call constructor
        Function(self._meta.init_detail[1]).with_args(
            Data.storage(MCF.storage), "call"
        )

        # pop stack
        pop_stack()

        # save back to class
        for shadow in self._meta.name_shadow_map.values():
            shadow.move(f"mem.{self._mcf_id}.{shadow._mcf_id}")

    def __construct__(self) -> None:
        """派生类应实现构造函数"""
        raise NotImplementedError

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
        """派生类应该自行实现NBT构造函数"""
        raise NotImplementedError

    def macro_construct(self, slot: str, mcf_id: str) -> Self:
        """默认宏构造函数"""
        temp: MCFVariable = self._meta.cls(init_val=None, void=True)
        temp._mcf_id = mcf_id
        Data.storage(MCF.storage).modify_set(f"mem.{mcf_id}", True).via(
            Data.storage(MCF.storage), f"mem.$({slot})"
        )
        return temp

    def duplicate(self, init_val: Any = None, void = False) -> Self:
        """产生MCFClass对象。

        注意：该方法并不能用于复制一个类的实例，该方法产生的实例仅保证MCFVariable的
        内部操作是可用的，不能保证编写的自定义类的方法同样可用。

        若需要复制一个自定义类，请在自定义类的`__init__`方法中做修改，使其支持复制
        操作。
        """
        return MCFClass(
            self._meta.cls,
            (),
            {"init_val": init_val, "void": void},
            self.__construct__
        )
    
    def rm(self):
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")
