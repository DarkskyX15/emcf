
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
    "gc": True
})

def main():
    string = text_to_string(Text("原神，启动！"))
    rev_str = string[::-1]
    say(string_to_text(rev_str))

if __name__ == '__main__':
    main()
