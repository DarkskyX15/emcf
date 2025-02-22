# states index: 116
data modify storage __st__ call.m2 set value "116"
# state: inverted, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h72396e7025e47dbe4a5c6fd0f52e57a8c455a807 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "inverted"
function block:get_index with storage __st__ call
# state: power, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/he5b803ff621bee01b53e4f201d270f6a21e952f4 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h39814854d6658a7cb190a8bf2602756bd38ee5ed run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hdc2d7905cd111377aac7d96d1bfab82c43880c21 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h3743357d7b3cdae6099afd57ecaf10e0197a5b66 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "power"
function block:get_index with storage __st__ call
