# states index: 72
data modify storage __st__ call.m2 set value "72"
# state: thickness, value_size: 5
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4246784827cd60d2fbfc2abb0d427bce8a730e83 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h6141fcaf5bc5b5580146c47e15cf4f37248edb9d run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h837b8c7ec29e760a0df3f698f332186e0adbd67a run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "thickness"
function block:get_index with storage __st__ call
# state: vertical_direction, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hda421b301077a019b60a913c2b6555d1d176c357 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "vertical_direction"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7ed45a43a644be409938e037c8342e4286a022e8 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
