
"""与HashMap相关的函数"""

from ..types import *
from ..functional import *
from ..control import *
from .string import *

__all__ = [
    'get_keys'
]

@MCFunction(ArrayList[Text])
def get_keys(hash_map: HashMap):
    """This is an expensive operation, use it with consideration."""
    map_string = text_to_string(hash_map.to_text().substr(1, -1))
    front = Integer(0)
    back = Integer(0)
    _in_text = Text("-")
    result = ArrayList()
    stack = ArrayList()
    with While()(back < map_string.size()):
        cur = map_string[back].to(Text)
        with If((cur == '"') | (cur == "'")):
            pre_index = back - 1
            with If(pre_index < 0):
                pre_index.assign(0)
            previous = map_string[pre_index].to(Text)
            with If(previous != '\\'):
                with If(_in_text != '-'):
                    _in_text.assign(cur)
                with Elif(_in_text == cur):
                    _in_text.assign('-')
            back += 1
        with Elif((cur == '{') | (cur == '[')):
            with If(_in_text == '-'):
                stack.append(cur)
            back += 1
        with Elif((cur == '}') | (cur == ']')):
            with If(_in_text == '-'):
                stack.pop(Text, -1)
            back += 1
        with Elif(cur == ':'):
            with If((_in_text == '-') & (stack.size() == 0)):
                result.append(string_to_text(map_string[front:back]))
            back += 1
        with Elif(cur == ','):
            with If((_in_text == '-') & (stack.size() == 0)):
                front.assign(back + 1)
            back += 1
        with Else():
            back += 1
    Return(result)

