# states index: 114
data modify storage __st__ call.m2 set value "114"
# state: shape, value_size: 10
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbfff2a560b6c33033da7e48f32ad41927b34c0e1 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3218d76f8dcd72b52d68dbe60d57905c08eb6d3e run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/he7cf9450541201e47d6a2acda7c12c944085a195 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h3a33730c12ba8b997a7747162cc23e3f8dfe8c52 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "shape"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4970feb55f686008df78abf52926982ac88719d1 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
