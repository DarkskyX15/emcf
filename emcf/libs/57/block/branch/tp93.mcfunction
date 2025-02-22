# states index: 93
data modify storage __st__ call.m2 set value "93"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hed72d0c9ca2eedeb185ab97262d8ac5a2e3862e3 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hcb5537e21d9514ef43bc37beb67da54908a8f945 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: mode, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hc847883f4e3aa220d6112043b7e5aac0276d8ecc run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "mode"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3a70d513927faf1e4931013f7f29ab9ffab2a98a run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
