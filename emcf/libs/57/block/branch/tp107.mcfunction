# states index: 107
data modify storage __st__ call.m2 set value "107"
# state: level, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb06fe4080ca8c4fc0954a1e15554567f916615bd run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h863d726358395c5fe5f8c462278e7cf73ba1c1a1 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "level"
function block:get_index with storage __st__ call
