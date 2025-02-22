# states index: 102
data modify storage __st__ call.m2 set value "102"
# state: tip, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf9d5d4881c524dbd313731c791c7829462029e87 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "tip"
function block:get_index with storage __st__ call
