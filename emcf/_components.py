
from .core import MCF

class BuiltinComponents:
    def __init__(self):
        pass

    def initialize(self) -> None:
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

builtin_components = BuiltinComponents()
MCF._builtin_cps = builtin_components
