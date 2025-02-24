
"""string相关的函数"""

from ..types import *
from ..control import *
from ..functional import *

__all__ = [
    'text_to_string',
    'string_to_text',
    'string_compare',
    'split_string'
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

@MCFunction(ArrayList[Text])
def split_string(string: ArrayList[Text], split: Text):
    result: ArrayList[Text] = ArrayList()
    front = Integer(0)
    back = Integer(0)
    text_size = string.size()

    with While()(back < text_size):
        with If(string[back].to(Text) == split):
            result.append(
                string_to_text(string[front:back])
            )
            front.assign(back + 1)
        back += 1
    result.append(
        string_to_text(string[front:back])
    )
    Return(result)

