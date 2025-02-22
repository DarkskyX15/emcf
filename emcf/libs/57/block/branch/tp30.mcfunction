# states index: 30
data modify storage __st__ call.m2 set value "30"
# state: conditional, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hae874800a37984cb9cc81545674c98aa6dea64d9 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "conditional"
function block:get_index with storage __st__ call
# state: facing, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hadad47cc57fdb398000adf67a3276ef7c6dd03d2 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h19cf0d8c229587af433602fcf2b74ef38ad92a4b run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h2f14dd8098eebb54bf5c1da353145939ab807725 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
