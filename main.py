
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
    s = Text('原神，启动！')
    arr = text_to_string(s)
    say(arr)
    ps = string_to_text(arr)
    say(ps)

if __name__ == '__main__':
    main()
