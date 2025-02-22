# states index: 79
data modify storage __st__ call.m2 set value "79"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h08a8d5c8a32dae3ed9069371971d8ece68d88f2e run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he4e0273e5e41dd531c77981682c74fdef8bc64c6 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: lit, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h81b6d5f89b55f3eef969ba81cc92de890b7bb881 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "lit"
function block:get_index with storage __st__ call
