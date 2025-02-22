# states index: 21
data modify storage __st__ call.m2 set value "21"
# state: level, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4cc061e1687bacf29029ce1dd23ba250f65f2800 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf14f7d3349cf25a7c9b1d82ece1dc0a2f8012f7b run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h4e98a5f996c6df60d487975850e27b187e9592b5 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h02eb2ce5c2a6aad43de7d2be0b9beb4b3d15cd3f run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "level"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5b560a42bb08ad2fd35c19ffdfd1cc332f4876e6 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
