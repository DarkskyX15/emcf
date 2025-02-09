execute if score __buf4__ __bd__ >= __buf2__ __bd__ run return fail
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __buf4__ __bd__
function al_ops:_slice/main with storage __st__ call
scoreboard players operation __buf4__ __bd__ += __buf3__ __bd__
function al_ops:_slice/pos_enter