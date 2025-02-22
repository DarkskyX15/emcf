# states index: 51
data modify storage __st__ call.m2 set value "51"
# state: power, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h2d60a381214debeceb5e9015ad92433a12f5f8b3 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he14b880311353d1e415a7f45a0184318e119ab72 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hdb37b0ad702d56360358aa539269a4f21e6461f1 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/hf8fddf75cc027f7f8a936a4d37e46f5242953e5d run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "power"
function block:get_index with storage __st__ call
# state: sculk_sensor_phase, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h342e323db8440e719abf42fd69f4d36f70cea457 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h13e92f6c89d4c9a6e0e9b78a8ce8bfb18e003c55 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "sculk_sensor_phase"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h86cebb7f3169e2eb8eae76c26de5c30b1e02ebb2 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
