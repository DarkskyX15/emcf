# states index: 24
data modify storage __st__ call.m2 set value "24"
# state: age, value_size: 8
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hafb9c65fa1e847ddaecef5a89f636d953cea3bcd run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hbfac1a4ff76fe8fdfa8b2d4e7b6118785fcf3373 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h715b57150838a13b7063a7701159cf61ffc9f2a3 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
