# states index: 109
data modify storage __st__ call.m2 set value "109"
# state: ominous, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbdc7183b229540ed251485f4c45c5e5df6bbd6b1 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "ominous"
function block:get_index with storage __st__ call
# state: trial_spawner_state, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h12534fc4defaeed090b7078b78b495f44b3224a7 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h6c8a16c2d01e9ad30b2816fae4780e36b38de931 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h33dc76513c1b56a455f9dda8b59d1dd94ffb88b6 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "trial_spawner_state"
function block:get_index with storage __st__ call
