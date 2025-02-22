# states index: 49
data modify storage __st__ call.m2 set value "49"
# state: bloom, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1397e205e667a5a4a10feee1c07ddfb8b2ff520f run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "bloom"
function block:get_index with storage __st__ call
