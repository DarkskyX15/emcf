# states index: 54
data modify storage __st__ call.m2 set value "54"
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/had85fceaaacc79c8b13f4b0089ae51028afa6182 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
# state: shape, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h0d908065d53739dd602a578123981b69a2fc5bd9 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hd6aa0265cc482244c3599d80e6a74be6711ddafd run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hc1b175bb996f0d38a86224a270bfc50061814b8d run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "shape"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb6cdce88db3244d1cd03b3e4b84ac10ae38bfca5 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
