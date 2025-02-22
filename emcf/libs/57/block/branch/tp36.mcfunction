# states index: 36
data modify storage __st__ call.m2 set value "36"
# state: hatch, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h43a176bfdb57613abaabc9c76b7b39b20120188e run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h6eab077b17eb6311b7377029ed21c23890889b13 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "hatch"
function block:get_index with storage __st__ call
