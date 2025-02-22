# states index: 8
data modify storage __st__ call.m2 set value "8"
# state: axis, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/ha30c6499bc8849ef92021f1fd766ee66a578f285 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h65204d1be4d27f3891073421af2dd40a895e78fd run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "axis"
function block:get_index with storage __st__ call
