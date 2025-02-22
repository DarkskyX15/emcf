# states index: 74
data modify storage __st__ call.m2 set value "74"
# state: age, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf5e951f4e6e120eee3aabdc0f45a03603539efc8 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he3fbbf3f57197bba33a4229b2409b5b661fc578f run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h79006c2dd60a504fec5d4e43746ece22a000797f run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h97c88f182ed6e32600c634dbc4cef6012986335e run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
# state: east, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd7918e369a83d85f414fb4513335a9f7f5cbf010 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "east"
function block:get_index with storage __st__ call
# state: north, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3b6fc8a685cc062776a88ef585327731589aef6b run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "north"
function block:get_index with storage __st__ call
# state: south, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd858083c82ec59635257a1752dd8bd08f7985834 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "south"
function block:get_index with storage __st__ call
# state: up, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h28b3c2afa48867845f30df4e0cbc4d41e079fe6e run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "up"
function block:get_index with storage __st__ call
# state: west, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h704f1edb1f158ff9df8ed243f228c21c4643b26f run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "west"
function block:get_index with storage __st__ call
