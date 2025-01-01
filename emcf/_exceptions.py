
from typing import Any

class MCFException(BaseException):
    def __init__(self, *args):
        super().__init__(*args)

class MCFVersionError(MCFException):
    message: str
    def __init__(self, info: str, version: str):
        super().__init__(info)
        self.message = f"{info}, present version: {version}"
    def __str__(self):
        return self.message

class MCFTypeError(MCFException):
    message: str
    def __init__(self, sign: str, val: Any):
        super().__init__(sign, val)
        self.message = sign.format(val)
    def __str__(self):
        return self.message

class MCFValueError(MCFException):
    message: str
    def __init__(self, msg: str):
        super().__init__(msg)
        self.message = msg
    def __str__(self):
        return self.message

class MCFComponentError(MCFException):
    message: str
    def __init__(self, msg: str):
        super().__init__(msg)
        self.message = msg
    def __str__(self):
        return self.message
