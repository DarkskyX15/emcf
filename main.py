
from emcf.core import MCF
from emcf.display import say
from emcf.selector import Selector
from emcf.types import *
from emcf.control import mcf_if

if __name__ == '__main__':

    MCF.useConfig({
        "namespace": "test",
        "version": 1204
    })

    val1 = Integer(10)
    val2 = Integer(20)
    val3 = Integer(30)

    with mcf_if:
        pass
    with mcf_elif:
        pass
    with mcf_else:
        pass

    val4 = Integer(val1 * val2 * val3)
    say(val4, Selector("@e"))

