
from typing import Any

__all__ = [
    'MCFException',
    'MCFVersionError',
    'MCFTypeError',
    'MCFValueError',
    'MCFComponentError',
    'MCFSyntaxError',
]

class MCFException(Exception):
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
    def __init__(self, *args: Any):
        if len(args) == 1:
            self.message = args[0]
        else:
            self.message = args[0].format(args[1])
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

class MCFSyntaxError(MCFException):
    message: str
    def __init__(self, msg: str):
        super().__init__(msg)
        self.message = msg
    def __str__(self):
        return self.message
