# states index: 105
data modify storage __st__ call.m2 set value "105"
# state: bites, value_size: 7
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h43a45d027a1c2e960b184ff6dce4135e648f1dac run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h9e0c26f28ebf91ab196b730cf9e6d46d5748fd81 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h3c248691de50d8fd616834618c7a921238bb577a run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "bites"
function block:get_index with storage __st__ call
