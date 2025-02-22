# states index: 44
data modify storage __st__ call.m2 set value "44"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h83710a77710cae7f8758c1ef4f67c3059f87f09b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h1f931045513aceb4c477cc7b385e0b0185a68c3f run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: lit, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4f27207dfa6f3fc2bc0d232e936e7687e413e518 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "lit"
function block:get_index with storage __st__ call
