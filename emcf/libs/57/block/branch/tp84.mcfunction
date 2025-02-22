# states index: 84
data modify storage __st__ call.m2 set value "84"
# state: face, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/he3464755e56760d85e659d01e78a9017a192bcd4 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h94017c6afbea9849744fbe0ac65dbbfe8cdcc5e5 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "face"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h24fefe3828040ba985fe312b259b31ee68cfeb3b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h6269817c3709b46f0297191225031ea42a403c4a run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
