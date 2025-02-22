# states index: 71
data modify storage __st__ call.m2 set value "71"
# state: eggs, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h49b21e1910a9b7e0c7b8640b5f9ac7a0a506aa7d run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hada9294cf258b09649a78a576808e0faa9fdf215 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "eggs"
function block:get_index with storage __st__ call
# state: hatch, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf097cf38ce1034a84215285d8aacf55a72119a8b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h251ef417777b1e51ee9cfeddbd62630dd435948c run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "hatch"
function block:get_index with storage __st__ call
