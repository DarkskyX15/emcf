# states index: 82
data modify storage __st__ call.m2 set value "82"
# state: age, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf8f728a7f18e147727dca36fb0b215a2c625fce5 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3ebf0133ebe48fac7a40edfa35679a08bc8555c5 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
