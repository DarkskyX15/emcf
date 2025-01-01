execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.v
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.v

# return in advance (x * 0 or 0 * x)
execute if score __buf1__ __bd__ matches 0 run return run function math_float_calc:ret_zero
execute if score __buf2__ __bd__ matches 0 run return run function math_float_calc:ret_zero

data modify storage __st__ register set value {}

scoreboard players operation __buf3__ __bd__ = __buf2__ __bd__
scoreboard players operation __buf3__ __bd__ += __buf1__ __bd__
scoreboard players set __cst__ __bd__ 9

scoreboard players operation __buf3__ __bd__ -= __cst__ __bd__
execute if score __buf3__ __bd__ matches ..-1 run scoreboard players set __buf3__ __bd__ 0
scoreboard players operation __buf4__ __bd__ = __buf3__ __bd__
scoreboard players set __cst__ __bd__ 2
scoreboard players operation __buf4__ __bd__ %= __cst__ __bd__
scoreboard players operation __buf3__ __bd__ /= __cst__ __bd__

# record
scoreboard players operation __buf5__ __bd__ = __buf1__ __bd__
scoreboard players operation __buf6__ __bd__ = __buf2__ __bd__
scoreboard players operation __buf5__ __bd__ -= __buf3__ __bd__
scoreboard players operation __buf6__ __bd__ -= __buf3__ __bd__

# record extra
execute if score __buf1__ __bd__ >= __buf2__ __bd__ run scoreboard players operation __buf5__ __bd__ -= __buf4__ __bd__
execute if score __buf1__ __bd__ < __buf2__ __bd__ run scoreboard players operation __buf6__ __bd__ -= __buf4__ __bd__

# extra reducer
scoreboard players operation __gen__ __bd__ = __buf4__ __bd__
function math_pow10:entry
scoreboard players operation __buf4__ __bd__ = __cst__ __bd__

scoreboard players set __cst__ __bd__ 0
execute if score __buf1__ __bd__ >= __buf2__ __bd__ run scoreboard players set __cst__ __bd__ 1

# get integer
execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.a
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.a

# extra reduction
execute if score __cst__ __bd__ matches 1 run scoreboard players operation __buf1__ __bd__ /= __buf4__ __bd__
execute if score __cst__ __bd__ matches 0 run scoreboard players operation __buf2__ __bd__ /= __buf4__ __bd__

# precision reduction
scoreboard players operation __gen__ __bd__ = __buf3__ __bd__
function math_pow10:entry
scoreboard players operation __buf1__ __bd__ /= __cst__ __bd__
scoreboard players operation __buf2__ __bd__ /= __cst__ __bd__

# do mul
scoreboard players operation __buf1__ __bd__ *= __buf2__ __bd__
scoreboard players operation __gen__ __bd__ = __buf1__ __bd__
function math_float_calc:count_size

# save a
execute store result storage __st__ register.a int 1.0 run scoreboard players get __buf1__ __bd__
# save v
execute store result storage __st__ register.v byte 1.0 run scoreboard players get __cst__ __bd__

# get e
execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.e
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.e

scoreboard players operation __buf1__ __bd__ += __buf2__ __bd__

scoreboard players operation __cst__ __bd__ -= __buf5__ __bd__
scoreboard players operation __cst__ __bd__ -= __buf6__ __bd__
scoreboard players add __cst__ __bd__ 1

scoreboard players operation __buf1__ __bd__ += __cst__ __bd__

# save e
execute store result storage __st__ register.e byte 1.0 run scoreboard players get __buf1__ __bd__
