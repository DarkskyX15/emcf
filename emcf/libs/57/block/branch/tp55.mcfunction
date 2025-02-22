# states index: 55
data modify storage __st__ call.m2 set value "55"
# state: lit, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h44da757c9671c9ed8e918fd2ab087468150adb8e run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "lit"
function block:get_index with storage __st__ call
