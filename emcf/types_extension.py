
"""基于MCFClass/MCFunction自举的扩展类型以及相关函数"""

from .types import *
from .classing import *
from .control import *
from .functional import *
from .display import say

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
        text.push_back(char)
    Return(text)

@MCFunction(Condition)
def string_compare(a: ArrayList[Text], b: ArrayList[Text]):
    with If(a.size() != b.size()):
        Return(Condition(False))
    index = Integer(0)
    size = a.size()
    for char in a.iterate(Text):
        with If(index >= size):
            Break()
        with If(char != b[index].to(Text)):
            Return(Condition(False))
        index += 1
    Return(Condition(True))
