# states index: 60
data modify storage __st__ call.m2 set value "60"
# state: power, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7bf0cb34fb64d91375451a331edb553d9b70c0d4 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he4c82750ca5dbf2d7ea5738523621eaf62b79d7e run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h6e79655b7d38134548af872f2cf5789a5f6cb958 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h5eb6de6b5b8e4aee0a0b6da5db12fbe107a93fa7 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "power"
function block:get_index with storage __st__ call
