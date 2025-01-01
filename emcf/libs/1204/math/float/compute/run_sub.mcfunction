# a - b -> a + (-b)
scoreboard players set __cst__ __bd__ -1
execute store result score __buf3__ __bd__ run data get storage __st__ cache.right.a
scoreboard players operation __buf3__ __bd__ *= __cst__ __bd__
execute store result storage __st__ cache.right.a int 1.0 run scoreboard players get __buf3__ __bd__

function math_float_calc:run_plus
