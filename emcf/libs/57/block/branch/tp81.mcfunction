# states index: 81
data modify storage __st__ call.m2 set value "81"
# state: age, value_size: 5
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h86f930bcf32b1aee8cdfa4009fe977c57335c03d run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h12c895bce903900010df728f9f51a7bb3bcb839a run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h930dc512f0d673a884776e1d1a02422d53637e39 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
# state: half, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbb1f58f9230654c08e44b48f08b43cddf431598c run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "half"
function block:get_index with storage __st__ call
