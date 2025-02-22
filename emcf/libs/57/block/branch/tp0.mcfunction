# states index: 0
data modify storage __st__ call.m2 set value "0"
# state: unstable, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h553f215da62a97ba32236e2f40c4177347e5ecb4 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "unstable"
function block:get_index with storage __st__ call
