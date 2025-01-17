
from emcf.core import MCF
from emcf._utils import console
from emcf.display import say
from emcf.selector import Selector
from emcf.classing import *
from emcf.types import *
from emcf.control import *
from emcf._writers import *
from emcf.functional import *
from typing import Annotated


MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": True
})

@MCFunction(FakeNone)
def test(x: IntegerRef, size: Integer):
    x += size

def main():
    x = Integer(10)
    say(x)
    test(Ref(x), Integer(10))
    say(x)
    test(Ref(x), Integer(20))
    say(x)
            
if __name__ == '__main__':
    main()

