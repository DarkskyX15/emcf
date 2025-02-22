# states index: 31
data modify storage __st__ call.m2 set value "31"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h2cfec868af3ad51f0a022acefad0afc8849882b0 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h1ea1789dae476e7f1f93a61b79fa65370ba25e9e run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7614f6b9c22ad3254bf5de2eb568399b8cd9b0f4 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "occupied"
function block:get_index with storage __st__ call
# state: part, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/haccb3b866b96a5dd28cd5202c0cb7bda5a572f43 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "part"
function block:get_index with storage __st__ call
