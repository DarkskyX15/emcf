# states index: 100
data modify storage __st__ call.m2 set value "100"
# state: age, value_size: 8
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hcadabc1a9433821a867b20edcb67d8fe9c346ece run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h5903ff36b132317956735b56a384dcc19f11fcb2 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h3813aeb2b0a5124969ee26ff8eae1667b33967f7 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
