# states index: 45
data modify storage __st__ call.m2 set value "45"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/ha5f9eacbee92c492795881da7b463beebfa4efe5 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/haf0d22c4cb79fc982419fbda99bdac03ad3d2bdd run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: tilt, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4bef3c236381fec1ba5ccb0ecc2156ad1b6ae8f9 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h0258e3a0c2bb175a1a55dbacb1c28fb386e73b18 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "tilt"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbdc3d98f2a173a378fdfe136d681beec1634c3dd run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
