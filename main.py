
from emcf.core import MCF
from emcf._utils import console
from emcf.display import say
from emcf.selector import Selector
from emcf.types import *
from emcf.control import *
from emcf._writers import *
from emcf.functional import MCFunction, Return


MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": True
})

@MCFunction(Float)
def test(x: Float) -> None:
    say(x)
    Return(x)

def main():
    var1 = Float(1.114)
    test(var1)
    with If(1):
        say(var1)
    with If(Condition(False)):
        say(666)
    with Else():
        say(555)

if __name__ == '__main__':
    main()

