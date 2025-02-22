# states index: 53
data modify storage __st__ call.m2 set value "53"
# state: orientation, value_size: 12
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h84de39333efd26de588920de0d0be87bd84e641a run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h1f9deca229855b2f5f7634d2ea6738bc33eb1374 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h90c28bb24a939146224a1ff4f0fdcc0f407fe6cf run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h365711fe0753f566c0929291ea09854ac7cc5ffe run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "orientation"
function block:get_index with storage __st__ call
