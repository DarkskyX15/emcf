# states index: 1
data modify storage __st__ call.m2 set value "1"
# state: half, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5ae1af426b40b33cbb366dbae8daa47fed6b880b run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "half"
function block:get_index with storage __st__ call
