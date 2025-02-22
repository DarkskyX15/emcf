# states index: 70
data modify storage __st__ call.m2 set value "70"
# state: pickles, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h35c93d55fbced508b1694f253ea5a85363168920 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h50d74897690b204614cf264201d554c453786174 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "pickles"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7fa81daf82d38e7015701d2bab4be3213984b6ac run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
