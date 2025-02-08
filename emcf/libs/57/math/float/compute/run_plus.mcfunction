data modify storage __st__ register set value {}
execute store result score __buf1__ __bd__ run data get storage __st__ cache.left.e
execute store result score __buf2__ __bd__ run data get storage __st__ cache.right.e
execute store result score __buf3__ __bd__ run data get storage __st__ cache.left.v
execute if score __buf3__ __bd__ matches 0 run return run function math_float_calc:ret_right
execute store result score __buf3__ __bd__ run data get storage __st__ cache.right.v
execute if score __buf3__ __bd__ matches 0 run return run function math_float_calc:ret_left

# buf1 -> left.e   buf2 -> right.e
execute if score __buf1__ __bd__ > __buf2__ __bd__ run return run function math_float_calc:plus/neg
execute if score __buf1__ __bd__ < __buf2__ __bd__ run return run function math_float_calc:plus/pos

# buf4 -> left.v   buf3 -> right.v
execute store result score __buf4__ __bd__ run data get storage __st__ cache.left.v
execute if score __buf4__ __bd__ <= __buf3__ __bd__ run return run function math_float_calc:plus/pos
function math_float_calc:plus/neg