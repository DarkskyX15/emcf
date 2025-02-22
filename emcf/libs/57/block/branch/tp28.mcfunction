# states index: 28
data modify storage __st__ call.m2 set value "28"
# state: dusted, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/he05f282ef2bab8741b8ecf4cb2669f92e0e4b9e2 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3609e2c5d6c6f2c9b2ff5d3d59c941ec2ed0f202 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "dusted"
function block:get_index with storage __st__ call
