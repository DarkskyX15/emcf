
from emcf.core import MCF
import emcf.v57.debug as debug
from emcf.types import *
from emcf.types_extension import *
from emcf.control import *
from emcf.functional import *
from emcf.bootstrapping.string import *
from emcf.bootstrapping.hash_map import *

MCF.useConfig({
    "namespace": "test",
    "version": 57,
    "gc": True
})

def main():
    example_map = HashMap({
        "key1": Integer(10),
        "key2": Float(1.114)
    })
    debug.log(example_map)
    keys = get_keys(example_map)
    debug.log(keys)

if __name__ == '__main__':
    main()
