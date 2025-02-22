# states index: 37
data modify storage __st__ call.m2 set value "37"
# state: axis, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hab0498107357a442f54d9c727af2c4eb852e7a1d run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h29daf72a5929deb12ed8a776220ab6881093388b run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "axis"
function block:get_index with storage __st__ call
# state: creaking_heart_state, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hce4bbec31f138468612e61857ec8b891fb21843b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h9d4269a131850fd3a566f807f566cda0a9dc95fb run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "creaking_heart_state"
function block:get_index with storage __st__ call
# state: natural, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h6b74a67b28e24ddd2635d03e5b26040ca33c972b run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "natural"
function block:get_index with storage __st__ call
