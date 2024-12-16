
from emcf.core import MCF
from emcf.basic import *

if __name__ == '__main__':

    MCF.useConfig({
        "namespace": "test",
        "version": 1204
    })

    val1 = Integer(10)
    val2 = Integer(20)
    val3 = Integer(30)

    val4 = Integer(val2 * val3)

