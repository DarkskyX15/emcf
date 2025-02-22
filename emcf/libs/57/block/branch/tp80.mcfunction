# states index: 80
data modify storage __st__ call.m2 set value "80"
# state: level, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h423ecfbc1fd264c0a599d4f39bf91ced0cfa5642 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/heb37ef4bea6ccbf174c6654ef087180baa8a1816 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/haa64827237d291cb4ff577d3dd1e8556edcb1f81 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h6e13924087fbf12c2987b3f4633c8f46d2c60112 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "level"
function block:get_index with storage __st__ call
