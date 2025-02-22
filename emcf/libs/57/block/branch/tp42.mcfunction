# states index: 42
data modify storage __st__ call.m2 set value "42"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/ha87f3f6294752a9ff114537b36b41d696d8d9a34 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h7036087bd3fae7c607530e75ca6627e4bfc3b0ff run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h6268ed6fac6173a32b452d427e7748dc8047b791 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
