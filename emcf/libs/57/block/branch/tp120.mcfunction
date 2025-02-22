# states index: 120
data modify storage __st__ call.m2 set value "120"
# state: instrument, value_size: 23
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hb9176d155d408f40b1343dbf992d3141fd1492de run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h747ad0fad3bdb42c282132c594a2f09744e70000 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/he24ac16beea75be85978292a1bb3c68b6ad4e99d run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h48e4fd54eb1f738080c5493bd4f4da90b6e2a511 run scoreboard players add __gen__ __bd__ 8
execute if predicate __nsp__:bp/sub/he0d290f37d02c789ddefde0717409fc496a37d0a run scoreboard players add __gen__ __bd__ 16
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "instrument"
function block:get_index with storage __st__ call
# state: note, value_size: 25
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/habbfbd9a98068e3b117299916c7c0661f9b1bb55 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h9f6bdcc700a0980df42d63b3953d4a24dd1c92e1 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/haa32c4995ce75c4b1d354c6986c458274ca99718 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h267971562eaddc16fa5fc8c8066c1483706c84ec run scoreboard players add __gen__ __bd__ 8
execute if predicate __nsp__:bp/sub/h9daa090e59f9ff62286d7bb108d23a1d83af2801 run scoreboard players add __gen__ __bd__ 16
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "note"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf72601d26a6fa93b0b3b3e45e3c690cd79e47987 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
