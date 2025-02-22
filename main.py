
from emcf.core import MCF
import emcf.v57.debug as debug
from emcf.types import *
from emcf.control import *
from emcf.functional import *
from emcf.types_extension import *
from emcf._writers import *


MCF.useConfig({
    "namespace": "test",
    "version": 57,
    "gc": True
})

def main():
    block = Block("~ ~-1 ~")
    block.query_state()
    debug.log(block)

if __name__ == '__main__':
    main()
