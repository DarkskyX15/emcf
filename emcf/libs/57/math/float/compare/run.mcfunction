
# sign judge
execute store result score __buf3__ __bd__ run data get storage __st__ cache.left.a
execute store result score __buf4__ __bd__ run data get storage __st__ cache.right.a
scoreboard players set __buf1__ __bd__ 1
scoreboard players set __buf2__ __bd__ 1
execute if score __buf3__ __bd__ matches ..-1 run scoreboard players set __buf1__ __bd__ -1
execute if score __buf4__ __bd__ matches ..-1 run scoreboard players set __buf2__ __bd__ -1

execute if score __buf1__ __bd__ > __buf2__ __bd__ run return run scoreboard players set __gen__ __bd__ 1
execute if score __buf1__ __bd__ < __buf2__ __bd__ run return run scoreboard players set __gen__ __bd__ -1

# e judge
execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.e
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.e
execute if score __buf1__ __bd__ > __buf2__ __bd__ run return run scoreboard players set __gen__ __bd__ 1
execute if score __buf1__ __bd__ < __buf2__ __bd__ run return run scoreboard players set __gen__ __bd__ -1

# same e, judge a then
# get v, fill up gap
execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.v
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.v

scoreboard players set __cst__ __bd__ -1
# 1 -> buf1.v >= buf2.v   0 -> buf1.v < buf2.v
scoreboard players set __buf6__ __bd__ 1
scoreboard players operation __buf1__ __bd__ -= __buf2__ __bd__
execute if score __buf1__ __bd__ matches ..-1 run scoreboard players set __buf6__ __bd__ 0
# abs(buf1)
execute if score __buf1__ __bd__ matches ..-1 run scoreboard players operation __buf1__ __bd__ *= __cst__ __bd__
scoreboard players operation __gen__ __bd__ = __buf1__ __bd__
function math_pow10:entry

# fill gap
execute if score __buf6__ __bd__ matches 1 run scoreboard players operation __buf4__ __bd__ *= __cst__ __bd__
execute if score __buf6__ __bd__ matches 0 run scoreboard players operation __buf3__ __bd__ *= __cst__ __bd__

# compare adjusted a
execute if score __buf3__ __bd__ > __buf4__ __bd__ run return run scoreboard players set __gen__ __bd__ 1
execute if score __buf3__ __bd__ < __buf4__ __bd__ run return run scoreboard players set __gen__ __bd__ -1

# equal
scoreboard players set __gen__ __bd__ 0

