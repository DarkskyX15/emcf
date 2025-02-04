
# load data
execute store result score __buf1__ __bd__ run data get storage __st__ register.a
execute store result score __buf2__ __bd__ run data get storage __st__ register.e
execute store result score __buf3__ __bd__ run data get storage __st__ register.v

scoreboard players operation __buf2__ __bd__ -= __buf3__ __bd__
scoreboard players add __buf2__ __bd__ 1
function math_float_ext:get_scale
function math_float_ext:apply with storage __st__ call
