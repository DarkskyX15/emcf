
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

    buf1 = "__buf1__"
    buf2 = "__buf2__"
    buf3 = "__buf3__"
    gen = "__gen__"
    bd = "__bd__"
    st = "__st__"
    namespace = "math_float_calc"

    var1 = Float(114.514)
    var2 = Float(0.0)

    say(Float._operate(var1, var2, '+'))
    say(Float._operate(var2, var1, '-'))

    MCF.exportComponents()
