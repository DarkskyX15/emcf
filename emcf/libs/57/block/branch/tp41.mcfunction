# states index: 41
data modify storage __st__ call.m2 set value "41"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1d73cfef34081609e33ac5642abbe4cd9eac27d8 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf1a1a618b90cbac021cad2f9650904c249531415 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h10832633198a34541409a5c37f03d33ba24069cd run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
