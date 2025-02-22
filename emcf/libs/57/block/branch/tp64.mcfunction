# states index: 64
data modify storage __st__ call.m2 set value "64"
# state: level, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5f217789a62e85120464128db90c026a77fe7bbb run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h29ff9f6bdfb31d23404ba4482bf1fcd59876c3e8 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h84e52d6154ea310398c1d12fce8e9023165f9f0e run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/hbde21ec236c6137d7033f199210db50f906858ab run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "level"
function block:get_index with storage __st__ call
