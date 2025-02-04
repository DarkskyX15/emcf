execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __buf1__ __bd__
function array_list:private/try_get with storage __st__ call
execute if score __gen__ __bd__ matches 0 run return 1
execute if score __gen__ __bd__ matches 1 run function array_list:private/append with storage __st__ call
scoreboard players add __buf1__ __bd__ 1
function array_list:private/extend_main