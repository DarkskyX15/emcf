# states index: 95
data modify storage __st__ call.m2 set value "95"
# state: east, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h48f8a39bfe54ede041e170f530ff8772d7bbb4a3 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h29f99d6024514aca153c2bd896ae306496d785e2 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "east"
function block:get_index with storage __st__ call
# state: north, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h882c74e3699ee003aaed616003f95a2dc6b61f4b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he18319ac6e904d20a43e4ed9ac0f8ae77a9c3d01 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "north"
function block:get_index with storage __st__ call
# state: power, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbba666128b4d07641f6fe643f4b0258e00a02957 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hc585af19fe55e1bc2184babfe3129bcc32c43211 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h299e8ce043cca848ff7bb95cf61147e3ce0e5835 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h8e1d03cfb9dd680d0f54683501987befa62b97a6 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "power"
function block:get_index with storage __st__ call
# state: south, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4a1da976eb74f7f93020f38fa770e989011ff3dc run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h61a9f412145fd7d57b88068fca0dbe70a0f0ff61 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "south"
function block:get_index with storage __st__ call
# state: west, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hfa124448b0eeb7da06fee60c237624a417dd9924 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h8d3f997993414a0f2c5f02ea6ee8b3963bc2e286 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "west"
function block:get_index with storage __st__ call
