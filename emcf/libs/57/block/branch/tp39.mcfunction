# states index: 39
data modify storage __st__ call.m2 set value "39"
# state: age, value_size: 26
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hfde9a12305ac38e5815d744f3e53031b5883ef14 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h4bd0c8d984fd9eb30ace4d2473a6bc5476c13578 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hab66abcfd47cc78e6d8e5030c73c0342aeab6020 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/hfaeb383c43fc27b3e7982f0406558a1fd3bd3fa8 run scoreboard players add __gen__ __bd__ 8
execute if predicate __nsp__:bp/sub/h917b8f63d6befbce8bac06b0a2eeaf574df309b6 run scoreboard players add __gen__ __bd__ 16
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
