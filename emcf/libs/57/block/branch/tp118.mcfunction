# states index: 118
data modify storage __st__ call.m2 set value "118"
# state: layers, value_size: 8
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hdee1f97acc8130b430034692ddd4e8fa0690f6c4 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3ff696932d6b13a2dfb0617acbc84be14bc696b8 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hcb7703e397c35bbfea3603e2f1f84fb694f17aef run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "layers"
function block:get_index with storage __st__ call
