# states index: 119
data modify storage __st__ call.m2 set value "119"
# state: age, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd047afe74e3ebbe671c613a03ac15cb7ec556a19 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hb0cf868ff44991261d14a6c6093e2ca1cf6cf1e6 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
