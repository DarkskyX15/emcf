
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

@MCFunction(Integer)
def fact(num: Integer) -> None:
    result = Integer(1)
    for index in Range(2, num + 1):
        result *= index
    Return(result)

def main():
    for index in Range(10, 0, -1):
        result = fact(index)
        say(result)
        with If(result < 5000):
            say("stop")
            Break()
            
if __name__ == '__main__':
    main()

