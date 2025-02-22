# states index: 92
data modify storage __st__ call.m2 set value "92"
# state: delay, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbe1e4322ec7833fea45b44e3a37696e3fec74fd7 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h852f4122b1c7eccc7e4d66154cb65d09ffc957e3 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "delay"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8f686bbf4a6d69f3ef666b8cd0c251849d3a70f3 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf008c4d426719825b758ce59220cc5f5c4422363 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: locked, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3276cc713414ed18aad4e2c51559001f1c7664e9 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "locked"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h682b4577120ff3581653e74f904937c7a894091e run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
