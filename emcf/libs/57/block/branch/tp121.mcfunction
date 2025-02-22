# states index: 121
data modify storage __st__ call.m2 set value "121"
# state: cracked, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbe5efe2d691902bea152225dfca31241eae9fba5 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "cracked"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hc2cf88d2ee4d140ddc788a6f29c130c132c3d67e run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hb29963ab88a64a1197dc5f7e9b32376de4d1b14d run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hca0d07c8d89b71d99cb85d9715d5011b6dd33b20 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
