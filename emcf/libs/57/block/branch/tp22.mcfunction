# states index: 22
data modify storage __st__ call.m2 set value "22"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hec64e9ecbe0ac9890cd7c6cb09d7dd344d97d79f run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h288f833fa6d0552a8048ee198eb567eaf4bc3220 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
