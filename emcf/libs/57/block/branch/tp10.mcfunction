# states index: 10
data modify storage __st__ call.m2 set value "10"
# state: rotation, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1f07eb9b381cf9d0390fc4441692563f43ac3a3b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3b067bd74735b8c715720c795c4d506a5b90fb87 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h06724f24ec95ba298613285a3b29acc28d23d532 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h9bf7b3bc8c09aed011703983ecfb3bd56d020074 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "rotation"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hcb14a28fbbb125a04074c8e43e8afbf4853e89a8 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
