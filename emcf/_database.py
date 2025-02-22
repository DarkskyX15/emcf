
from ._utils import getMultiPaths, console
from ._exceptions import MCFComponentError
from typing import Callable
import json, os, sys

__all__ = [
    'MCFDataBase',
]

SLASH = os.path.sep

class MCFDataBase:
    _mcf_path: str
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

        # load version database
        # TODO
        with open(path, 'r') as file:
            self.selectors = json.loads(file.readline())
    
    def validateSign(self, sign: str) -> bool:
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
        callback: Callable[[dict[str, list[str]]], None],
        cp_init_path: str
    ) -> None:
        symbol_map: dict[str, dict[str, list[str]]] = {}
        requires_map: dict[str, list[str]] = {}
        on_init_map: dict[str, str] = {}
        static_map: dict[str, list[dict[str, str]]] = {}

        for component in self._loaded_cps:
            cp_path = os.path.join(self._path, *component.split('.'))
            config_path = os.path.join(cp_path, "component.json")
            # config surely exists
            with open(config_path, 'r', encoding='utf-8') as rd:
                config = json.loads(rd.read())
            # config json should be a dict
            if not isinstance(config, dict):
                console.error(
                    MCFComponentError(
                        f"Invalid format for component.json in component '{component}'"
                    )
                )
            # load config
            namespace = config.get('namespace', 'local')
            requires_map[component] = config.get('requires', [])
            init_function = config.get('onInitialize', None)
            statics = config.get('static', None)
            if init_function is not None:
                on_init_map[component] = f"{namespace}:{init_function}"
            if statics is not None:
                static_map[component] = statics
            # get all mcfunction in component
            files, _ = getMultiPaths(cp_path)
            files = [file for file in files if file.endswith('.mcfunction')]
            # resolve all mcfunction
            signature_mapping: dict[str, list[str]] = {}
            # file path
            for file in files:
                rel = os.path.relpath(file, cp_path).removesuffix('.mcfunction')
                # sign
                sub_cp_id = component + '.' + '.'.join(rel.split(SLASH))
                # signature
                sub_func_sig = f"{namespace}:{'/'.join(rel.split(SLASH))}"
                signature_mapping[sub_cp_id] = [sub_func_sig, file]
            callback(signature_mapping)
            symbol_map[component] = signature_mapping

        # replace & write
        on_init_wt = open(cp_init_path, "w", encoding='utf-8')
        for component in symbol_map.keys():
            macros = self._cps_macros[component]
            replacements = []
            for key, value in macros.items():
                replacements.append((f"__{key}__", value))
            requires = [component]
            requires.extend(requires_map[component])
            init_func_name = on_init_map.get(component, '')
            for required in requires:
                for infos in symbol_map[required].values():
                    replacements.append((infos[0], infos[3]))
                    if infos[0] == init_func_name:
                        on_init_wt.write(
                            f"function {infos[3]}\n"
                        )
            # temporary fix for replace strategy
            # sort in descending order
            replacements.sort(key=lambda c: len(c[0]), reverse=True)
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
        on_init_wt.close()

        # write static files
        for component in self._loaded_cps:
            cp_path = os.path.join(self._path, *component.split('.'))
            static_requests = static_map.get(component, [])
            macro_map = self._cps_macros.get(component, {})
            for request in static_requests:
                rq_type = request["type"]
                src_path = os.path.join(cp_path, request["src"])
                dist_prefix = request["dist"]
                dist_path = os.path.normpath(
                    os.path.join(self._mcf_path, *rq_type.split('.'), dist_prefix)
                )
                file_path, folder_path = getMultiPaths(src_path)
                file_path = [file for file in file_path if file.endswith('.json')]
                for folder in folder_path:
                    rel = os.path.relpath(folder, src_path)
                    new_dir = os.path.normpath(
                        os.path.join(dist_path, rel)
                    )
                    os.makedirs(new_dir, exist_ok=True)
                for file in file_path:
                    rel = os.path.relpath(file, src_path)
                    new_file = os.path.normpath(
                        os.path.join(dist_path, rel)
                    )
                    with (open(file, 'r', encoding='utf-8') as rd, 
                        open(new_file, 'w', encoding='utf-8') as wt):
                        while line := rd.readline():
                            for target, replacer in macro_map.items():
                                line = line.replace(f"__{target}__", replacer)
                            wt.write(line)

    def pushComponent(self, cp_id: str, macros: dict[str, str]) -> bool:
        if cp_id in self._loaded_cps:
            # already loaded
            return True
        if cp_id not in self._available_cps:
            # not an available component
            return False
        self._loaded_cps.add(cp_id)
        self._cps_macros[cp_id] = macros
        return True

