# states index: 115
data modify storage __st__ call.m2 set value "115"
# state: axis, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h01dc2fd7ff097fe0184e70bb1e251411a2ceb9fc run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf8929a114c6bb72b11c784a7ec0d406af9c3abdd run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "axis"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5890e5ee3e69d81f4ebb904ae0472a9db0fed476 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
