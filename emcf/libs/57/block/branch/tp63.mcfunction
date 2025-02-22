# states index: 63
data modify storage __st__ call.m2 set value "63"
# state: drag, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf98a949dacdd9a1f8b730b2873a201065daeb657 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "drag"
function block:get_index with storage __st__ call
