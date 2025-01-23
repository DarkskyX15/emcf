
from emcf.core import MCF
from emcf._utils import console
from emcf.display import say
from emcf.selector import Selector
from emcf.classing import *
from emcf.types import *
from emcf.control import *
from emcf._writers import *
from emcf.functional import *
from emcf.classing import *
from gc import get_referrers


MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": True
})

class Inner(MCFClass):
    number: Integer
    def __init__(self, *args, **kwargs):
        super().__init__(Inner, args, kwargs)
    def __construct__(self, num: Integer):
        self.number.assign(num)
    def increase(self, step: Integer) -> FakeNone:
        self.number += step

class Fib(MCFClass):
    a1: Integer
    a2: Inner
    def __init__(self, *args, **kwargs):
        super().__init__(
            Fib, args, kwargs
        )
    def __construct__(self, s1: Integer, s2: Inner):
        self.a1.assign(s1)
        self.a2.assign(s2)
    def increase(self) -> FakeNone:
        self.a2.increase(self.a1)
    def show(self) -> FakeNone:
        say(self.a2.number)

@MCFunction(FakeNone)
def test(fib: Fib):
    say(fib)

def main():
    fib = Fib(Integer(10), s2=Inner(Integer(2)))
    fib2 = Fib(Integer(1), Inner(Integer(10)))
    for index in Range(5):
        fib.increase()
        fib2.increase()
    fib.show()
    fib2.show()
    test(fib)
    test(fib2)
            
if __name__ == '__main__':
    main()

