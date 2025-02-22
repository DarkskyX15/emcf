# states index: 75
data modify storage __st__ call.m2 set value "75"
# state: age, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5f00b325ec158f47c24e6b19cc1568a38e2b1d7d run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
