
"""基于MCFClass/MCFunction自举的扩展类型以及相关函数"""

from .types import *
from .classing import *
from .control import *
from .functional import *

__all__ = [
    'text_to_string',
    'string_to_text',
    'string_compare'
]

@MCFunction(ArrayList[Text])
def text_to_string(text: Text):
    string = ArrayList()
    for index in Range(0, text.size()):
        string.append(
            text.substr(index, index + 1)
        )
    Return(string)

@MCFunction(Text)
def string_to_text(string: ArrayList[Text]):
    text = Text()
    for char in string.iterate(Text):
        text.concat(char)
    Return(text)

@MCFunction(Condition)
def string_compare(a: ArrayList[Text], b: ArrayList[Text]):
    a_size = a.size()
    b_size = b.size()
    with If(a_size != b_size):
        Return(Condition(False))
    for index in Range(a_size):
        with If(a[index].to(Text) != b[index].to(Text)):
            Return(Condition(False))
    Return(Condition(True))
