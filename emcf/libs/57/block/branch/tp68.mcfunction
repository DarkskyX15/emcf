# states index: 68
data modify storage __st__ call.m2 set value "68"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/he505126c258e33c3ef2b7aee001ea6dd6b1fb673 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hea61648a353ffa593b0114ec53e094fa8e248078 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h178ea12e57467ca806ae0de26a1b231f9ddecadf run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: short, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h0a2ae1737c37506fb8ca21c65e72820fb46282b5 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "short"
function block:get_index with storage __st__ call
# state: type, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hcf72ddb43144d03f8d071e983415f7e8258508d5 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "type"
function block:get_index with storage __st__ call
