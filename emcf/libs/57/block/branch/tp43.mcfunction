# states index: 43
data modify storage __st__ call.m2 set value "43"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf913500cd369a942f6894e0406f3bf849f8eb56f run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h679d9aa2df4d9890dc1212c72b8ae588f729c2dd run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5c7dec5ad198d59f7680d8d087fca3efbd80d772 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
