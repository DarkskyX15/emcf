# states index: 5
data modify storage __st__ call.m2 set value "5"
# state: east, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hcddea0816f2ff0fc04e50d5e7538374e8b630934 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h3d19e807793774cfc602003e54cffa81d1a7e9bf run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "east"
function block:get_index with storage __st__ call
# state: north, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h418291da7bdc3454de3a8361fe4bd65e99cd64ca run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hffea2558c7d4e1348014dba0f2b5f3bcf69e2d0d run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "north"
function block:get_index with storage __st__ call
# state: south, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h6a099b935652643af56e9f958eafaf71c747877f run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h6cf0009a76a1aeac14a48fe1998d947786d612e6 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "south"
function block:get_index with storage __st__ call
# state: up, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h64e89caac9ba432d02ff76c77bd1c12bd965f454 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "up"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hc89ddd6c6c246f1b82428480f64d0393bf1c6380 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
# state: west, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h4ace2e7500a725fea2bc0c43170029d5592595b3 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he4110fa1571fa8f3d60ed70883a8deb14702e887 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "west"
function block:get_index with storage __st__ call
