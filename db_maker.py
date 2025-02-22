
import json

if __name__ == '__main__':

    contents = []

    for i in range(2, 9):
        size = 1 << ((8 - i) * 4)
        s = f"""# pos {i} {size}
scoreboard players set __cst__ __bd__ {size}
scoreboard players operation __buf2__ __bd__ = __gen__ __bd__
scoreboard players operation __buf2__ __bd__ /= __cst__ __bd__
scoreboard players operation __gen__ __bd__ %= __cst__ __bd__
function entity:_uuid/get_repr
data modify storage __st__ cache.r{i} set from storage __st__ register"""
        contents.append(s)
        

    with open('func.mcfunction', 'w', encoding='utf-8') as wt:
        wt.write('\n\n'.join(contents))
