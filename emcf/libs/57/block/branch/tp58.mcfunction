# states index: 58
data modify storage __st__ call.m2 set value "58"
# state: eye, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/haefab4e65373db892c868ac2092ed5551162e01a run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "eye"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8cc67bef26900493fdcc073a36c3f0b4e256c1e2 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h02c9f4d61eb23e396338d3dc21ea851b22b3675a run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
