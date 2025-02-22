# states index: 3
data modify storage __st__ call.m2 set value "3"
# state: age, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd09ae4f9d2882bc6ddeba8a5d2cc76fa9ab5631c run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h0817181a6676d875aac1a367f7c696361625e2e5 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
