# states index: 112
data modify storage __st__ call.m2 set value "112"
# state: charges, value_size: 5
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd11a045b14be46495617be4ca41bba2aae7ca6e0 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hc4d2b20859c5b79bbef3c4efbc5d2b7aa02bf5ce run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h9c555e30aa8a7fc00ff5161489de56aaf9c5ebed run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "charges"
function block:get_index with storage __st__ call
