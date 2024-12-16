
import json, os

class MCFDataBase:
    selectors: list[str]
    
    def __init__(self, version: int):
        cur_dir = os.path.dirname(__file__)
        path = os.path.join(cur_dir, f".\\db\\{version}.json")
        with open(path, 'r') as file:
            self.selectors = json.loads(file.readline())
