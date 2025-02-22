# states index: 19
data modify storage __st__ call.m2 set value "19"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/he8583cf65e06ff0e93db2971fdc6ee147cda224a run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h735c695542fdeba66baa30ba8494368cce7e96c0 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h3c88daae795174916f9d9c5d565d2446287bf212 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h2d5ca87d2afe4a5b9eb40fae5fa0be03fe5af75b run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
