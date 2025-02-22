# states index: 90
data modify storage __st__ call.m2 set value "90"
# state: age, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hfb7d751712017281a476f14ee55dbc49330b2804 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/ha1bc8795fdec8fd16c6a9e806acffc4d01d79449 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hd0b466aaf52539d906c23c580b68ebb96dd9e051 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
