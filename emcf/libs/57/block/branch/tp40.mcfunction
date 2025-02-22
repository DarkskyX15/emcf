# states index: 40
data modify storage __st__ call.m2 set value "40"
# state: level, value_size: 9
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h66c41059847d8bcb9f8f010846b8642552945b34 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h974d453d30ce9b4acc73bbbb591ee433321182b5 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h6c7059cfa3b15bbf2aa93e74fc69207e76cbf77f run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h1fdc6c8660f43f39b8f24b7fc98438f30a86e072 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "level"
function block:get_index with storage __st__ call
