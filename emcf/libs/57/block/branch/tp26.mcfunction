# states index: 26
data modify storage __st__ call.m2 set value "26"
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h9748b0d0ee5d01eb2dcdf4629fa5731726d2ee6c run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h4596ef5fa9fa82966c1aadcab5c4929a7a74ddd5 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/ha2a8c6766bf471a26ca0517750aa36ec0c3adc86 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: triggered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb2c026f0abfc25735a4b8c87333c6b221437e55f run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "triggered"
function block:get_index with storage __st__ call
