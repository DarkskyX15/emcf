# states index: 83
data modify storage __st__ call.m2 set value "83"
# state: age, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h28493eaf3448406ce872ac3f64b8dfaccc0fcfd1 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h51086c3b7e9fcc8e7534263f8fac1d2aa33166d1 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
