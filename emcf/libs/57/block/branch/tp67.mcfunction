# states index: 67
data modify storage __st__ call.m2 set value "67"
# state: extended, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h84a186a9a21baed7c7846dd8512b306c5f260105 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "extended"
function block:get_index with storage __st__ call
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb27502695b9621e0c3728ad6571041c404b4d1d1 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h8051369f5cbb07a9495799fe26720d40ffb1a2d5 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hecf1a610f3db14b5512f9e68d1eb9f86ae89f541 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
