# states index: 11
data modify storage __st__ call.m2 set value "11"
# state: face, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h332b94da77b52b5f841fcc03371e9d7a28c0aa31 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h28f2fff4d2c493accf9b7c7ac4b771fee7776278 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "face"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hc34c7e47c16886c77dca7b7aba8e8d26ccef287c run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h8b761165337ce29a342a435dbe1cfa8df86e17e1 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8d21492dae404122e223d0d16eb6e266f5355093 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
