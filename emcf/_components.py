
from .core import MCF, MCFCore

class BuiltinComponents:
    def __init__(self):
        pass

    def initialize(self, _core: MCFCore) -> None:
        self.math_pow10 = {
            "src": MCF.GENERAL,
            "dist": MCF.CALC_CONST,
            "src_bd": MCF.sb_sys
        }

        self.float_construct = {
            "dist": MCF.GENERAL,
            "dist2": MCF.BUFFER1,
            "dist3": MCF.BUFFER2,
            "dist4": MCF.BUFFER3,
            "cst": MCF.CALC_CONST,
            "bd": MCF.sb_sys,
            "st": MCF.storage
        }

        self.float_compute = {
            "cst": MCF.CALC_CONST,
            "buf1": MCF.BUFFER1,
            "buf2": MCF.BUFFER2,
            "buf3": MCF.BUFFER3,
            "buf4": MCF.BUFFER4,
            "buf5": MCF.BUFFER5,
            "buf6": MCF.BUFFER6,
            "gen": MCF.GENERAL,
            "bd": MCF.sb_sys,
            "st": MCF.storage
        }

        self.float_extract = {
            "buf1": MCF.BUFFER1,
            "buf2": MCF.BUFFER2,
            "buf3": MCF.BUFFER3,
            "bd": MCF.sb_sys,
            "st": MCF.storage
        }

        self.float_compare = {
            "cst": MCF.CALC_CONST,
            "buf1": MCF.BUFFER1,
            "buf2": MCF.BUFFER2,
            "buf3": MCF.BUFFER3,
            "buf4": MCF.BUFFER4,
            "buf5": MCF.BUFFER5,
            "buf6": MCF.BUFFER6,
            "gen": MCF.GENERAL,
            "bd": MCF.sb_sys,
            "st": MCF.storage
        }

        self.array_list = {
            "st": MCF.storage,
            "bd": MCF.sb_sys,
            "buf1": MCF.BUFFER1,
            "buf2": MCF.BUFFER2,
            "buf3": MCF.BUFFER3,
            "buf4": MCF.BUFFER4,
            "cst": MCF.CALC_CONST,
            "gen": MCF.GENERAL
        }

        self.string = {
            "st": MCF.storage,
        }

        self.hash_map = {
            "st": MCF.storage,
            "bd": MCF.sb_sys,
            "gen": MCF.GENERAL
        }

        self.entity = {
            "st": MCF.storage,
            "bd": MCF.sb_sys,
            "gen": MCF.GENERAL,
            "cst": MCF.CALC_CONST,
            "buf1": MCF.BUFFER1,
            "buf2": MCF.BUFFER2,
            "buf3": MCF.BUFFER3
        }

        self.block = {
            "st": MCF.storage,
            "nsp": MCF._namespace,
            "bd": MCF.sb_sys,
            "gen": MCF.GENERAL
        }

builtin_components = BuiltinComponents()
MCF.initializeHelper(builtin_components.initialize)
