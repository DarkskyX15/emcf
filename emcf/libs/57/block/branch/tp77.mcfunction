# states index: 77
data modify storage __st__ call.m2 set value "77"
# state: snowy, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd185e52de154f5f3a4a1a27d0f0c15d1a641b278 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "snowy"
function block:get_index with storage __st__ call
