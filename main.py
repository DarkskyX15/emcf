
from emcf.core import MCF, embed_mcf
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
    embed_mcf([
        'say 1'
    ])
    h = HashMap({
        "qwq": Integer(10),
        "pwp": Integer(114)
    })
    keys = get_keys(h)
    debug.log(keys)

if __name__ == '__main__':
    main()
