
from typing import Any
from .core import MCF

class MCFException(BaseException):
    def __init__(self, *args):
        super().__init__(*args)

class MCFVersionError(MCFException):
    message: str
    def __init__(self, info: str):
        super().__init__(info)
        self.message = f"{info}, present version: {MCF._mcf_version}"
    def __str__(self):
        return self.message

class MCFTypeError(MCFException):
    message: str
    def __init__(self, sign: str, val: Any):
        super().__init__(sign, val)
        self.message = sign.format(val)
    def __str__(self):
        return self.message

class MCFNameError(MCFException):
    message: str
    def __init__(self, val: str):
        super().__init__(val)
        self.message = f"MCF id not found: {val}"
    def __str__(self):
        return self.message

class MCFValueError(MCFException):
    message: str
    def __init__(self, msg: str):
        super().__init__(msg)
        self.message = msg
    def __str__(self):
        return self.message
