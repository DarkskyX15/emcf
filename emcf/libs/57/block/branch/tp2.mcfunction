# states index: 2
data modify storage __st__ call.m2 set value "2"
# state: axis, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h44c5cff2ddb1f4de049f24bd8aac9375fef63cdb run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "axis"
function block:get_index with storage __st__ call
