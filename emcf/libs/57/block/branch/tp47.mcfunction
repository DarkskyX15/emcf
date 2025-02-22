# states index: 47
data modify storage __st__ call.m2 set value "47"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h0642305df7c1122d746e5fb779390b0409dacc53 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h77aabbd2501c7f242cfc0096a58f172253be64c5 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: ominous, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1c14bc4d4d58b97e5682d682fc66564655642c18 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "ominous"
function block:get_index with storage __st__ call
# state: vault_state, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb6e2af05174aca8048adbad71eded470529af679 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h5be80b17f0a54d4c4284686522b3dd18ecff014f run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "vault_state"
function block:get_index with storage __st__ call
