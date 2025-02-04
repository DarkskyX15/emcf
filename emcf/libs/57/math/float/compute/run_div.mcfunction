execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.v
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.v
execute store result score __buf3__ __bd__ run data get storage __st__ cache.left.a
execute store result score __buf4__ __bd__ run data get storage __st__ cache.right.a

# return in advance
execute if score __buf1__ __bd__ matches 0 run return run function math_float_calc:ret_zero
execute if score __buf2__ __bd__ matches 0 run return run function math_float_calc:ret_zero

data modify storage __st__ register set value {}

# fill up
scoreboard players set __cst__ __bd__ 9
scoreboard players operation __cst__ __bd__ -= __buf1__ __bd__
scoreboard players operation __gen__ __bd__ = __cst__ __bd__
function math_pow10:entry
scoreboard players operation __buf3__ __bd__ *= __cst__ __bd__

# cut down
scoreboard players operation __buf5__ __bd__ = __buf2__ __bd__
scoreboard players remove __buf5__ __bd__ 4
execute if score __buf5__ __bd__ matches ..-1 run function math_float_calc:div/neg_fill
execute if score __buf5__ __bd__ matches 0.. run function math_float_calc:div/pos_fill

# do div
scoreboard players operation __buf3__ __bd__ /= __buf4__ __bd__

# save a
execute store result storage __st__ register.a int 1.0 run scoreboard players get __buf3__ __bd__

scoreboard players operation __gen__ __bd__ = __buf3__ __bd__
function math_float_calc:count_size

# save v
execute store result storage __st__ register.v int 1.0 run scoreboard players get __cst__ __bd__
scoreboard players remove __cst__ __bd__ 6

execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.e
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.e

scoreboard players operation __buf1__ __bd__ -= __buf2__ __bd__
scoreboard players operation __buf1__ __bd__ += __cst__ __bd__

# save e
execute store result storage __st__ register.e int 1.0 run scoreboard players get __buf1__ __bd__

