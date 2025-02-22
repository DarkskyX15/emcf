# states index: 35
data modify storage __st__ call.m2 set value "35"
# state: has_record, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1b5d7850a83ce678cc74139e22cb9c6f8a462a16 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "has_record"
function block:get_index with storage __st__ call
