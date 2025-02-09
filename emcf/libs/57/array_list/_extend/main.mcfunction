execute if score __gen__ __bd__ >= __cst__ __bd__ run return fail
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
function al_ops:_extend/operate with storage __st__ call
scoreboard players add __gen__ __bd__ 1
function al_ops:_extend/main