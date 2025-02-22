# states index: 7
data modify storage __st__ call.m2 set value "7"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5d18f34a264d315d694a1c5beb8763901994c2bd run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h10879597063ede747e7bade4a8dea9293f415439 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: half, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hcf8f41f4737d5caf810068f88fbec6a907534a1a run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "half"
function block:get_index with storage __st__ call
# state: shape, value_size: 5
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hbcc63b6fc7bc7489f898dd68d80957035917d3f4 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h8e406f1978136a70ed854f00ad4252f7bd0b94ad run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/h48949d34bd0db0df09aa62130f3e72990ff8f356 run scoreboard players add __gen__ __bd__ 4
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "shape"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hea52c970e63f1cd7b62fee2727308108a3ed06d6 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
