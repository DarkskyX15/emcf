
from ._utils import getMultiPaths
from ._exceptions import MCFComponentError
from typing import Callable
import json, os, sys

__all__ = [
    'MCFDataBase',
]

SLASH = '\\' if sys.platform.startswith('win') else '/'

class MCFDataBase:
    _path: str
    _loaded_cps: set[str]
    _available_cps: set[str]
    _cps_macros: dict[str, dict[str, str]]

    selectors: list[str]
    
    def __init__(self, version: int):
        self._loaded_cps = set()
        cur_dir = os.path.dirname(__file__)
        path = os.path.join(cur_dir, f"./libs/{version}/db.json")
        path = os.path.normpath(path)
        self._path = os.path.join(cur_dir, f"./libs/{version}")
        self._path = os.path.normpath(self._path)
        
        files, _ = getMultiPaths(self._path)
        files = [
            os.path.relpath(file, self._path)
            .removesuffix(f'{SLASH}component.json')
            .replace(SLASH, '.')
            for file in files if file.endswith('component.json')
        ]
        self._available_cps = set(files)
        self._cps_macros = dict()

        with open(path, 'r') as file:
            self.selectors = json.loads(file.readline())
    
    def validateSign(self, sign: str) -> None:
        paras = sign.split('.')
        sign_path = os.path.join(self._path, *paras) + '.mcfunction'
        if not os.path.exists(sign_path):
            return False
        parent = paras[0]
        for para in paras[1:]:
            if parent in self._available_cps:
                break
            parent += f".{para}"
        if parent not in self._loaded_cps:
            return False
        return True

    def writeComponents(
        self,
        callback: Callable[[dict[str, list[str]]], None]
    ) -> None:
        symbol_map: dict[str, dict[str, list[str]]] = {}
        requires_map: dict[str, list[str]] = {}
        for component in self._loaded_cps:
            cp_path = os.path.join(self._path, *component.split('.'))
            config_path = os.path.join(cp_path, "component.json")
            with open(config_path, 'r', encoding='utf-8') as rd:
                config = json.loads(rd.read())
            if not isinstance(config, dict):
                raise MCFComponentError(
                    f"Invalid format for component.json in component '{component}'"
                )
            namespace = config.get('namespace', 'local')
            requires_map[component] = config.get('requires', [])
            files, _ = getMultiPaths(cp_path)
            files = [file for file in files if file.endswith('.mcfunction')]
            signature_mapping: dict[str, list[str]] = {}
            sub_cps: list[str] = []
            for file in files:
                rel = os.path.relpath(file, cp_path).removesuffix('.mcfunction')
                sub_cp_id = component + '.' + '.'.join(rel.split(SLASH))
                sub_cps.append(sub_cp_id)
                sub_func_sig = f"{namespace}:{'/'.join(rel.split(SLASH))}"
                signature_mapping[sub_cp_id] = [sub_func_sig, file]
            callback(signature_mapping)
            symbol_map[component] = signature_mapping
        for component in symbol_map.keys():
            macros = self._cps_macros[component]
            replacements = []
            for key, value in macros.items():
                replacements.append((f"__{key}__", value))
            requires = [component]
            requires.extend(requires_map[component])
            for required in requires:
                for infos in symbol_map[required].values():
                    replacements.append((infos[0], infos[3]))
            for infos in symbol_map[component].values():
                with open(infos[1], 'r', encoding='utf-8') as rd:
                    lines = rd.read().splitlines()
                    to_write: list[str] = []
                    for line in lines:
                        if not line or line[0] == '#': continue
                        for key, replacer in replacements:
                            line = line.replace(key, replacer)
                        to_write.append(line + '\n')
                with open(infos[2], 'w', encoding='utf-8') as wt:
                    wt.writelines(to_write)

    def pushComponent(self, cp_id: str, macros: dict[str, str]) -> bool:
        if cp_id in self._loaded_cps:
            return True
        if cp_id not in self._available_cps:
            return False
        self._loaded_cps.add(cp_id)
        self._cps_macros[cp_id] = macros
        return True

