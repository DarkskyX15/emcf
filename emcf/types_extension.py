
from .types import *
from .classing import *
from .control import *
from typing import TypeVar, NewType, Generic, Iterable, Optional, Any

__all__ = [
    'Array'
]

ElemType = TypeVar("ElementType")
class Array(MCFVariable, Generic[ElemType]):
    def __init__(
        self,
        arr: Optional[Iterable[MCFVariable]],
        **kwargs: Any
    ):
        init_val = kwargs.get("init_val", None)
        void = kwargs.get("void", False)
        super().__init__(init_val, void)
        if void: return
        

Array[int]
