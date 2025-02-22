# states index: 106
data modify storage __st__ call.m2 set value "106"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h3d7fafa3fd6d6dfa0c60b6dc0a721d252401bcd5 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h0291e25a284bbd66d4a055009975643d42f2821e run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: honey_level, value_size: 6
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5d3c7075f45d4e47d389f11b077371ad1bb1cf07 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h4ab09b467ea01912cb3fe2d3f89bd45be71d883f run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h108d7e4f81ada3423de83ddcf9ba0b9ae3184f06 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "honey_level"
function block:get_index with storage __st__ call
