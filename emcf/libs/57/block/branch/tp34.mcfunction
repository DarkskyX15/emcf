# states index: 34
data modify storage __st__ call.m2 set value "34"
# state: candles, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hf2cbbaed074994c3ebb46a0cf6893d810b66457a run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/ha87d2446fa488dd28e72c1681a8b82ed26cbfe63 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "candles"
function block:get_index with storage __st__ call
# state: lit, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5274ba92b9497df25be40aa247e05dc8d1bf4a3a run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "lit"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbf6f7af95fbd9421a87a5a37105eaf29e1eec43c run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
