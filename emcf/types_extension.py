
"""基于MCFClass/MCFunction自举的扩展类型以及相关函数"""

from .types import *
from .classing import *
from .control import *
from ._writers import *
from ._exceptions import *
from ._components import builtin_components as builtin_cps
from ._utils import iterable, console
from .core import MCF
from .display import *
from .functional import *
from typing import (
    TypeVar, NewType, Generic, Iterable, Optional, Any, TypeAlias,
    Type, Annotated, get_args, get_origin
)


__all__ = [
    'text_to_string',
    'string_to_text',
    'string_compare'
]

@MCFunction(ArrayList[Text], (Text, ))
def text_to_string(text: Text):
    string = ArrayList(Text)
    for index in Range(0, text.size()):
        string.append(
            text.substr(index, index + 1)
        )
    Return(string)

@MCFunction(Text)
def string_to_text(string: ArrayList[Text]):
    text = Text()
    for char in string:
        text.push_back(char)
    Return(text)

@MCFunction(Condition)
def string_compare(a: ArrayList[Text], b: ArrayList[Text]):
    with If(a.size() != b.size()):
        Return(Condition(False))
    size = a.size()
    for index in Range(size):
        with If(a[index] != b[index]):
            Return(Condition(False))
    Return(Condition(True))
