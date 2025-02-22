# states index: 23
data modify storage __st__ call.m2 set value "23"
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h408160fb677cf18dc49dd972535be3397ba24e52 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
# state: shape, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h85a28527d215adb2675571ae1f8f40b757fe3a3e run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h5a89f3cc0a538346c13be4149ae5984e68f9f35e run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hb9157b455ed7186c10cc27c8431ad1193be7e6cb run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "shape"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8624fa97ce923262717a1f89171ccecbd2a005d8 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
