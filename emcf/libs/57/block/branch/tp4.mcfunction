# states index: 4
data modify storage __st__ call.m2 set value "4"
# state: type, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hc22091a1c4231ac32b9705fa5b4bf0b4bbf5cee9 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h555a7cfcac1ccbd380c9485a132198aad9c33754 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "type"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h70c7f732a841b08cb5ebabf99ea3543a19ebfee3 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
