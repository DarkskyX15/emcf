
import os, traceback
from typing import Any

__all__ = [
    'getMultiPaths',
    'LogOutput'
]

def getMultiPaths(folder_path: str) -> tuple[list[str], list[str]]:
    file_path_list = list()
    folder_list = list()
    for filepath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path_list.append(os.path.join(filepath, filename))
        folder_list.append(filepath)
    return (file_path_list, folder_list)

_RED = '\x1b[31m'
_GREEN = '\x1b[32m'
_YELLOW = '\x1b[33m'
_RESET = '\x1b[0m'

class LogOutput:
    _warn_cnt: int
    _error_cnt: int
    _err_override: bool
    _module_dir: str
    _working_dir: str

    def __init__(self):
        self._warn_cnt = 0
        self._error_cnt = 0
        self._err_override = True
        self._module_dir = os.path.split(__file__)[0] + os.path.sep
        self._working_dir = os.getcwd() + os.path.sep    

    def disableExceptionOverride(self) -> None:
        self._err_override = False

    def info(self, *infos: Any, sep: str = ' ') -> None:
        print('\x1b[0m[Info] ' + sep.join([str(info) for info in infos]))

    def warn(self, warning: str):
        self._warn_cnt += 1
        print('\x1b[33m[Warn] ' + warning)

    def error(self, err: Exception):

        def _cut_str(msg: str) -> str:
            if len(msg) >= 40: return '...' + msg[len(msg) - 37:]
            return msg

        if not self._err_override: raise err
        self._error_cnt += 1
        print(f'\x1b[31m[Error] \x1b[1m{type(err).__name__}: {err.__str__()}\x1b[0m')
        print(f'\t█ Traceback (most recent call first):')
        stack = traceback.extract_stack()
        topped = False
        for idx in range(len(stack) - 2, -1, -1):
            file, line, func, name = stack[idx]
            file: str
            if not file.startswith(self._module_dir):
                if file.startswith(self._working_dir):
                    fnt = '┃' if idx != 0 else '┗'
                    if not topped:
                        print(f'\t\x1b[31m┣━ {os.path.split(file)[1]} [top level]')
                        print(f'\t\x1b[31m┃\x1b[0m  File {file} in {func}')
                        print(f'\t\x1b[31m┃\x1b[0m\t{line}| {name}\n\t\x1b[31m{fnt}\x1b[0m')
                        topped = True
                    else:
                        print(f'\t\x1b[33m┣━ {os.path.split(file)[1]}')
                        print(f'\t\x1b[33m┃\x1b[0m  File {file} in {func}')
                        print(f'\t\x1b[33m┃\x1b[0m\t{line}| {name}\n\t\x1b[33m{fnt}\x1b[0m')
                else:
                    print(f'\t\x1b[0m┇ [other files] {_cut_str(file)} in {func}, line {line}')
            else:
                print(f'\t┃ {file.removeprefix(self._module_dir)} in {func}, line {line} [EMCF]')
        print(_RESET, end='')

    def summarize(self) -> None:
        print(_RESET)
        if self._error_cnt <= 0:
            if self._warn_cnt <= 0:
                # no err no warn
                print(f"{_GREEN}Compilation succeeded.{_RESET}")
            else:
                # just warnings
                print(f"{_YELLOW}Compilation succeeded but with {self._warn_cnt} warnings.{_RESET}")
        else:
            # have error
            print(f'{_RED}Compilation failed with {self._error_cnt} errors and {self._warn_cnt} warnings.{_RESET}')

console = LogOutput()
