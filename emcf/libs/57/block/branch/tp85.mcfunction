# states index: 85
data modify storage __st__ call.m2 set value "85"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3c3518e0d4aeef2868941b5302fd8c7bc4963054 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hc5897352d838434db6e9c42d5cf37a0eeeb3828f run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/ha4c80de9af75a1f42d5cb5cda07b17f908935a62 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: type, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd0564526dd5a26eb0b072cb5925d4cf3fda43390 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "type"
function block:get_index with storage __st__ call
