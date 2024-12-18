
import os

def getMultiPaths(folder_path: str) -> tuple[list[str], list[str]]:
    file_path_list = list()
    folder_list = list()
    for filepath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path_list.append(os.path.join(filepath, filename))
        folder_list.append(filepath)
    return (file_path_list, folder_list)