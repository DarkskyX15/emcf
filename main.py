
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
from emcf.types_extension import *


MCF.useConfig({
    "namespace": "test",
    "version": 57,
    "gc": False
})

def main():
    val = Float(114.514)
    val2 = Float(114.114)
    _map = HashMap({
        "val": val,
        "sec": val2
    })
    got = _map.get(Float, "sec", Float(0))
    got += val2
    _map.set("now", got)
    say(_map)

if __name__ == '__main__':
    main()
