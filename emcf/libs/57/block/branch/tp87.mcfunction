# states index: 87
data modify storage __st__ call.m2 set value "87"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hda5187587147e5aa4b661b1743eaa7734caa5850 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3fef1071ca26125a0f5dae9f5cae9826181043f9 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: type, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h62ebec29be50bb0871deffae752a912d2726c557 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h4da20d29e361459482ab396edab674d73976f596 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "type"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h1511c96263cdb2e0c7db41f6b2ea221daf3ddc93 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
