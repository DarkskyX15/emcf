# states index: 12
data modify storage __st__ call.m2 set value "12"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h710705c5cba028949b445b21e64fe0a98aab4223 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h19607dc59d8d6a4de3026aa48ca20cafc399429e run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: in_wall, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/heb90c222d2cc3e0be5d332e05bc6e28d376cf778 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "in_wall"
function block:get_index with storage __st__ call
# state: open, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h293865332de921d23807ffda2317ca2018db0b33 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "open"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h471116527360546b1bb4bb81f8e61c76d08e15d2 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
