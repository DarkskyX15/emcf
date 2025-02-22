# states index: 110
data modify storage __st__ call.m2 set value "110"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h01f91de45ca7a464dc87f9d709f337dc3a80d4d3 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h0ac2c154e9b5ebdbb5657b97f05629f7215b4604 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h30bc3760cc3b69aacb1668e0ff851aeda5ba59c1 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h6dadfb11844df2ea22d62efba335a895a252926e run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hca1345a68811f1eb3ca52bcb0846ba35fe51f62d run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
