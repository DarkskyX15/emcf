
from emcf.core import MCF
from emcf.display import say
from emcf.selector import Selector
from emcf.types import *
from emcf.control import *
from emcf.functional import MCFunction, Return

MCF.useConfig({
    "namespace": "test",
    "version": 1204,
    "gc": True
})

if __name__ == '__main__':

    var1 = Float(1.1145)
    var2 = Float(1.11)

    say(var1 > var2)
    say(var1 <= var2)

    MCF.exportComponents()