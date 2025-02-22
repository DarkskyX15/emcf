# states index: 91
data modify storage __st__ call.m2 set value "91"
# state: age, value_size: 5
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h860ced7aca2527aea133a178b7cde0558c6c1281 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h5a98ca1ec759bc4fa436a7a353c0425abddcafca run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h3bdf545d10f46636e9a54eef38e476defaffa4b2 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
# state: hanging, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4b21e2dc3df66063f9d00f03c465f7629f91a9e7 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "hanging"
function block:get_index with storage __st__ call
# state: stage, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hdc2c9003ce7c396694dde4b41d695ff775081f5e run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "stage"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hcb28c978e8e126c84e963f5d3d7cecfce5c1b2a7 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
