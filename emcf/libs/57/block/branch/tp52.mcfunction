# states index: 52
data modify storage __st__ call.m2 set value "52"
# state: attached, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h629afe776d693b5e24a876c0bcad5791087e0404 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "attached"
function block:get_index with storage __st__ call
# state: rotation, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbd99874ff7242815d6014c2d2a9c79d8a3cc4a40 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h99dce0daf06d05ed6fdc5ebe3d90c9c7e732054e run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h8339f35bc2c10eab238558b8c5bf6530f1a1cea8 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/hbc1a848292839fe8c530d8db8fe1faef33c49e79 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "rotation"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h50e247e3f220fdd66e4d128466aecdfcb4efbd70 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
