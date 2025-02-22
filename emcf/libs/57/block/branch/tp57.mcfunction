# states index: 57
data modify storage __st__ call.m2 set value "57"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1fe6bac5bb5a7cc6f38fb09a1d6a98fa9ca47685 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he8caaee01949615ffc60d14fcbcf1198ade5235e run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h1d42057b365672340a3a559966931531ae938897 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: open, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h49425394a78dc3453b6bbc8acb99f96571a7b01c run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "open"
function block:get_index with storage __st__ call
