
from emcf.core import MCF
from emcf.display import say
from emcf.selector import Selector
from emcf.types import *
from emcf.control import mcf_if
from emcf.functional import MCFunction


MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": True
})

@MCFunction
def test2(var: Integer) -> None:
    test2(var)

@MCFunction
def test3(var: Integer) -> None:
    say(var, Selector("@a"))

@MCFunction
def test(var: Integer, var2: Integer) -> None:
    test2(var)
    test3(var2)
    say(var2 + var)
    
if __name__ == '__main__':

    test(Integer(10), Integer(20))

    # val1 = Integer(10)
    # val2 = Integer(20)
    # val3 = Integer(30)

    # val4 = abs((val1 + val3) // val2 * 114 % val1)
    # say(val4, Selector("@e"))

    # c1 = (val1 < 10).Or(val2 > 19).And(val1 != val2).And(val1 == 10)
    # say(c1, Selector("@s"))
