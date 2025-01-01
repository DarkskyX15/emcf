
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

if __name__ == '__main__':

    var1 = Integer(11)

    var3 = Float(var1) / 0.1514
    var4 = 114.514 * var3

    say(var4)

    MCF.exportComponents()
