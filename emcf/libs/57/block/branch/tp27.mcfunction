# states index: 27
data modify storage __st__ call.m2 set value "27"
# state: age, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3ec49d518fafa9da34879d34baa4700d4b94e433 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h83eeba0822572b387ecb932c2147d8eb15b36585 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7f820772c38660aef99704e4e1b5826b6e82bb5b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h201d41290459876f7aa5e6d9a87b224a8875b327 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
