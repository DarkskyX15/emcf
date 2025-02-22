# states index: 32
data modify storage __st__ call.m2 set value "32"
# state: rotation, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8bd34ef6ad9aef6b2067edca5dda0e6884e66f25 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h899cfca86e4f904921f6367123d2ce77730095a9 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h2a50cb973e962071891c65ca8c7bd49518ddd25f run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h1f732b504cca94358c63fa1e694863326d542dcf run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "rotation"
function block:get_index with storage __st__ call
