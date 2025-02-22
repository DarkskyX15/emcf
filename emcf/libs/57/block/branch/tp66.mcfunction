# states index: 66
data modify storage __st__ call.m2 set value "66"
# state: berries, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4c9fbc12f11f294a949791eac3e965df9a291538 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "berries"
function block:get_index with storage __st__ call
