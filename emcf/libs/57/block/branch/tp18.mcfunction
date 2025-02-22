# states index: 18
data modify storage __st__ call.m2 set value "18"
# state: age, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h899a1d6516aa2b014dc3b5a27243767832fae60b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h667b4a09707f9a84458f8943234c1aea9203fc44 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h91f5a1ae35f45d796db9ea6d55ea6058b4956f72 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/hf579738aa1553d1549317ec25981f49c381aed33 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
