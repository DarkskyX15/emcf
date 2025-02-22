# states index: 73
data modify storage __st__ call.m2 set value "73"
# state: enabled, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb1282b3177308a6c488d154074c92082056df7c4 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "enabled"
function block:get_index with storage __st__ call
# state: facing, value_size: 5
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hce4daf53efee8b217020be6160b66d894a3cc081 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/ha26996fcb019a637240f41936199dfe73132062e run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h86cc39ed7bae3c101e2b5895647461d40466ac5e run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
