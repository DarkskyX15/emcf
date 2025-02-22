# states index: 15
data modify storage __st__ call.m2 set value "15"
# state: distance, value_size: 7
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h039a3fae901977ac02feb94f1a6f672c5cad7a2e run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h0bf7911874f0c720cb07b84f28a301974f9e4006 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hc53cc3b00f4c6439f32890ee716fac7c07ef2b55 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "distance"
function block:get_index with storage __st__ call
# state: persistent, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h665b14ded3a35fd22df3c872f89a063f2016fbcc run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "persistent"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1b907d6eea93fcb79307ed9063de5d7094684d18 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
