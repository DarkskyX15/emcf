# states index: 113
data modify storage __st__ call.m2 set value "113"
# state: attachment, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h516201e94adbd787882cf0d08592579b19a5e239 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hdaa11c663c678283e1d003e8a189476b3806644a run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "attachment"
function block:get_index with storage __st__ call
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hd74a27b3be25e5580474d20322b15fce7cd17a20 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he3f7e35880004e282dbf2ed16eace57e834eeea4 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: powered, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h2e5ef8ab1ac63ccd2c19ef014808e4f5380c7a2b run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "powered"
function block:get_index with storage __st__ call
