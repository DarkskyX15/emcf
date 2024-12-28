
from ._utils import getMultiPaths
import json, os

class MCFDataBase:
    _path: str
    _loaded_cps: set

    selectors: list[str]
    
    def __init__(self, version: int):
        self._loaded_cps = set()
        cur_dir = os.path.dirname(__file__)
        path = os.path.join(cur_dir, f".\\libs\\{version}\\db.json")
        self._path = os.path.join(cur_dir, f".\\libs\\{version}")
        with open(path, 'r') as file:
            self.selectors = json.loads(file.readline())
    
    def loadComponent(self, cp_id: str) -> list[tuple[str, str]]:
        if cp_id in self._loaded_cps:
            return []
        self._loaded_cps.add(cp_id)
        path = self._path + '\\' + '\\'.join(cp_id.split('.'))
        files, _ = getMultiPaths(path)
        result = []
        for file in files:
            name = os.path.basename(file).split('.')[0]
            result.append((file, f"{cp_id}.{name}"))
        return result

