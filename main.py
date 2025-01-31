
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
    "version": 1204,
    "gc": True
})

def main():
    arr = ArrayList(Long, [Integer(i) for i in range(5)])
    say(arr)
    for number in arr:
        say(number)
    say(arr[::-1])
    for number in arr[::-1]:
        say(number * 10)

if __name__ == '__main__':
    main()
