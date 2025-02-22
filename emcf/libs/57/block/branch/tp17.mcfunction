# states index: 17
data modify storage __st__ call.m2 set value "17"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hdf816fbe48239f3cf38082ed9cc817d188369211 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hb24f5df1e9975e02b7a78d50e48c289ae220301d run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h8c84089117cb359bc1b451880386db14f9c6ec88 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3ac42abb8090844461f696e5995f01e1a1e63a36 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
