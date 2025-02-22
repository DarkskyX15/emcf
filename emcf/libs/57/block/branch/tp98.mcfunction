# states index: 98
data modify storage __st__ call.m2 set value "98"
# state: mode, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1693419201f98d8b43276f42ca2ec227185c6b7b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/had881ff9923166a0e69381f36a09d2ea6b228492 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "mode"
function block:get_index with storage __st__ call
