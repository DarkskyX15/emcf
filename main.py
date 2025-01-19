
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


MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": True
})

class Fib(MCFClass):
    a1: Integer
    a2: Integer
    def __init__(self, **kwargs):
        super().__init__(
            Fib, kwargs,
            a1=Integer(1),
            a2=Integer(1)
        )
        self.complete()
    def step(self) -> FakeNone:
        temp = self.a1 + self.a2
        self.a1.assign(self.a2)
        self.a2.assign(temp)
    def get(self) -> Integer:
        Return(self.a2)

def main():
    fib = Fib()
    for _ in Range(29):
        fib.step()
        say(fib.get())
    say(fib.get())
            
if __name__ == '__main__':
    main()

