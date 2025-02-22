# states index: 88
data modify storage __st__ call.m2 set value "88"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hef85a26b428ecc66f4ae8236b8fe356ef82a6bbe run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h60c47375ccc401a28718d90193597c3c8b136290 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: flower_amount, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h345c7e350e4f62041b527c296f2f8fb34e632588 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h8dcccedf091357e3da360c353b1ade59f3dce2e9 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "flower_amount"
function block:get_index with storage __st__ call
