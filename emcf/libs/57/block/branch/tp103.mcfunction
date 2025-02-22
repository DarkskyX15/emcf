# states index: 103
data modify storage __st__ call.m2 set value "103"
# state: bottom, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h7c54eb4d843dd7e10f590da6167cfd4fba1a83f5 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "bottom"
function block:get_index with storage __st__ call
# state: east, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5b03b0d8f54e3802908153c57b72a93ca04efb3c run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h2e4fd75598d394094ece98b694bf10b430a14f38 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "east"
function block:get_index with storage __st__ call
# state: north, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h0dab1eaaa70e888343f8507b18c5f9b0febcd2ef run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he14e1bf36d0e4aee0dddfb4e4f43eaeb235219c7 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "north"
function block:get_index with storage __st__ call
# state: south, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h74e9f22ffb6cf8a6ee948fd1402f07b3e33ce63b run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hb2ea3e6e785e2fa55f2f50f8ed70d2d19e9c06be run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "south"
function block:get_index with storage __st__ call
# state: west, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/heeab2663a7ae21a01856de80dca174c484920632 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h9eaf9abd16f71c926eaf933c4d137598fcbf2849 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "west"
function block:get_index with storage __st__ call
