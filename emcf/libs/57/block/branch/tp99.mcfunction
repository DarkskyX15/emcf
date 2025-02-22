# states index: 99
data modify storage __st__ call.m2 set value "99"
# state: moisture, value_size: 8
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h40a646194601b1b11fb4a6d3fc0bbc5eb508609b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hd974cf049d009fe92709cd35442938f35e4f0026 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hb3db7f6cd7beae7696492744e9258b3ef3f286e2 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "moisture"
function block:get_index with storage __st__ call
