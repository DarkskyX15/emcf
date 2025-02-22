# states index: 29
data modify storage __st__ call.m2 set value "29"
# state: crafting, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf40c1e0b1d330e277d3add0ebbcd3341b80af7ce run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "crafting"
function block:get_index with storage __st__ call
# state: orientation, value_size: 12
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3955d0a5f53e9cbd4e36d91866a24b2e56e301d5 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h1ca5440bd63195ccc8e1ce072cb02d53863fd3c0 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h4d5005363f2d41a7f62d6696680a10fd0a890da0 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h47ef58531385ae161334c598b3d07ecf76fdb6e8 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "orientation"
function block:get_index with storage __st__ call
# state: triggered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h396331fb608785fba2850ab77971b1b5b703ffdf run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "triggered"
function block:get_index with storage __st__ call
