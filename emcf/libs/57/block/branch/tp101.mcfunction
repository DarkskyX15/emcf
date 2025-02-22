# states index: 101
data modify storage __st__ call.m2 set value "101"
# state: bottom, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf87b405375e2879e6d4df94fd74e6ce2f6a21190 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "bottom"
function block:get_index with storage __st__ call
# state: distance, value_size: 8
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h207fabdf18a37db6af250577de44d6ccfad29b97 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h7b6ba4d58740ee2985dcbf83d21ba5d6f9bad38a run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h55683b78d79c56e135c79394b8b5cef02a62296b run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "distance"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h31f662161a86b11023d643615c7998b6e92cea1c run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
