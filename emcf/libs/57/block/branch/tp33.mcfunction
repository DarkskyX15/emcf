# states index: 33
data modify storage __st__ call.m2 set value "33"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7ad2a46891c16681eb930700fc7a4a555a9c707a run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hc25c84f17b8085fb4470a14ee40d281a12db6783 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h4958680b1d2e5d219a4fc2c7397aabe1e0e36365 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
