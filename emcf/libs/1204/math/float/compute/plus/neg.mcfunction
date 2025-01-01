scoreboard players operation __buf2__ __bd__ -= __buf1__ __bd__
execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.v
scoreboard players operation __buf2__ __bd__ += __buf1__ __bd__
execute store result score __buf1__ __bd__ run data get storage __st__ cache.right.v
scoreboard players operation __buf2__ __bd__ -= __buf1__ __bd__
scoreboard players operation __gen__ __bd__ = __buf2__ __bd__

# 有效长度
scoreboard players operation __buf2__ __bd__ += __buf1__ __bd__
scoreboard players operation __buf4__ __bd__ = __buf2__ __bd__

scoreboard players set __cst__ __bd__ 9
scoreboard players operation __buf2__ __bd__ -= __cst__ __bd__

# 判断是否需要减少精度
execute if score __buf2__ __bd__ matches ..-1 run scoreboard players set __buf2__ __bd__ 0
scoreboard players operation __gen__ __bd__ -= __buf2__ __bd__

# 扩大常数
function math_pow10:entry
execute store result score __buf1__ __bd__ run data get storage __st__ cache.right.a

# 补齐后第一个加数
scoreboard players operation __buf1__ __bd__ *= __cst__ __bd__

# 减小常数
scoreboard players operation __gen__ __bd__ = __buf2__ __bd__
function math_pow10:entry
execute store result score __buf3__ __bd__ run data get storage __st__ cache.left.a
scoreboard players operation __buf3__ __bd__ /= __cst__ __bd__

# 相加
scoreboard players operation __buf3__ __bd__ += __buf1__ __bd__

# tidy up
execute store result score __buf1__ __bd__ run data get storage __st__ cache.right.e
scoreboard players operation __gen__ __bd__ = __buf3__ __bd__
function math_float_calc:count_size
scoreboard players operation __buf2__ __bd__ = __cst__ __bd__
scoreboard players operation __buf2__ __bd__ -= __buf4__ __bd__
execute unless score __cst__ __bd__ matches 0 run scoreboard players operation __buf1__ __bd__ += __buf2__ __bd__
execute if score __cst__ __bd__ matches 0 run scoreboard players set __buf1__ __bd__ 0
scoreboard players set __buf2__ __bd__ 10
execute if score __cst__ __bd__ matches 10.. run scoreboard players operation __gen__ __bd__ /= __buf2__ __bd__
execute if score __cst__ __bd__ matches 10.. run scoreboard players remove __cst__ __bd__ 1

execute store result storage __st__ register.a int 1.0 run scoreboard players get __gen__ __bd__
execute store result storage __st__ register.e byte 1.0 run scoreboard players get __buf1__ __bd__
execute store result storage __st__ register.v byte 1.0 run scoreboard players get __cst__ __bd__
