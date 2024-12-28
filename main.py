
from emcf.core import MCF
from emcf.display import say
from emcf.selector import Selector
from emcf.types import *
from emcf.control import *
from emcf.functional import MCFunction, Return

MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": False
})

@MCFunction(Integer)
def fibonacci(num: Integer):
    with Mif((num == 1).Or(num == 2)):
        Return(Integer(1))
    Return(fibonacci(num - 1) + fibonacci(num - 2))

if __name__ == '__main__':

    var = Integer(30)

    result = fibonacci(var)
    say(result, Selector("@a"))


