# states index: 111
data modify storage __st__ call.m2 set value "111"
# state: has_bottle_0, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h86ff4137129b50df3039872cda7511b2d631aea9 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "has_bottle_0"
function block:get_index with storage __st__ call
# state: has_bottle_1, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5bad395bb1a9600ae700bc1ad735292df35f529f run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "has_bottle_1"
function block:get_index with storage __st__ call
# state: has_bottle_2, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h66c48f85762e902e7451ea1a5a5aed0eab18e58f run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "has_bottle_2"
function block:get_index with storage __st__ call
