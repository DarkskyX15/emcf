# states index: 69
data modify storage __st__ call.m2 set value "69"
# state: mode, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb6306b96d642df7829671fba1165e58c3a84a510 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h44268416391615fa8dd13a1941c0908a6e036314 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "mode"
function block:get_index with storage __st__ call
