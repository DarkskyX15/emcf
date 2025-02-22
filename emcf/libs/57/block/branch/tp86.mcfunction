# states index: 86
data modify storage __st__ call.m2 set value "86"
# state: age, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h341265ea6f8e032cab368d69d9d74e75e0138713 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
# state: leaves, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h023f6ba6fc4e477302fc47c456e4a4f90212c5fa run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h220aaa94536eea0f4ac0240a4f97739d796f653b run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "leaves"
function block:get_index with storage __st__ call
# state: stage, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h186c538f3a7e7945e3e675af372288295646159b run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "stage"
function block:get_index with storage __st__ call
