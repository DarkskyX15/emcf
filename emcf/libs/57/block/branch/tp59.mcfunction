# states index: 59
data modify storage __st__ call.m2 set value "59"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4e96c52e9e05ee7223a6d2a8c1bce6868f24e59f run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hfbaa4e176fe66c40ee123c7e0cc941d3ffa6a415 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: segment_amount, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h63f82238fd13a8d2ad02987a156bb3ca436ed9d1 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf79238df0ab711aae13a362f47df87fcd8c291c6 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "segment_amount"
function block:get_index with storage __st__ call
