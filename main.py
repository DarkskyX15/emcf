
from emcf.core import MCF
import emcf.v57.debug as debug
from emcf.types import *
from emcf.control import *
from emcf.functional import *
from emcf.types_extension import *


MCF.useConfig({
    "namespace": "test",
    "version": 57,
    "gc": True
})

def main():
    t1 = Text('"原神，启动"')
    t2 = Text("'哈哈'")
    arr = ArrayList([t1, t2])
    debug.log(arr)

if __name__ == '__main__':
    main()
