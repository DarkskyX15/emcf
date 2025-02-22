# states index: 20
data modify storage __st__ call.m2 set value "20"
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/haa7a2d11ed4ba2b4b81956ae71b4b52586430227 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
# state: rotation, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h979c408b7f91c774ee56f31527467f75c121d546 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h766b521ed5aa388ab592acb33c417655d5b1de36 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h567639fc38e9d614bcb8dbacaa122bd7e34dbdf0 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h778450cd0127f161659f41a8910f82bd5d945a0a run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "rotation"
function block:get_index with storage __st__ call
