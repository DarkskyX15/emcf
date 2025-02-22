# states index: 16
data modify storage __st__ call.m2 set value "16"
# state: stage, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8c0a00463acca8022c62f6060951cc796c2410ae run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "stage"
function block:get_index with storage __st__ call
