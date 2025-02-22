scoreboard players set __gen__ __bd__ 0
function block:_states/count
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
function block:_states/get_info with storage __st__ call
data modify storage __st__ cache.result set value {}

# block name
data modify storage __st__ cache.result.name set from storage __st__ register.n

# check block entity
execute store result score __gen__ __bd__ run data get storage __st__ register.e
execute if score __gen__ __bd__ matches 1 run data modify storage __st__ cache.result.block_entity set from block ~ ~ ~

# prepare to call branch
execute store success score __gen__ __bd__ run data get storage __st__ register.p
execute if score __gen__ __bd__ matches 0 run return 1

# set dict
data modify storage __st__ cache.result.block_states set value {}
data modify storage __st__ call.m0 set from storage __st__ register.p
function block:_states/run_branch with storage __st__ call

