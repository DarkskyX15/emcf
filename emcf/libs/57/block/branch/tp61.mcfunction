# states index: 61
data modify storage __st__ call.m2 set value "61"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h043360902bb2cae22a097540a5345d443ed07e6d run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h7ff842df61cb36defdbb56cbfbd734e9fe71dcdd run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: power, value_size: 16
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hfbbaae264f452dc7c4a223a970f0410305a6726a run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/h7a4cce81374a088a398ca5f32e6addda38762b2f run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/hf55b795a280def8f8b9cc948a4bb6a600357743b run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h6677c4cab8e02d116e041ee4c922e70c3fc30413 run scoreboard players add __gen__ __bd__ 8
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "power"
function block:get_index with storage __st__ call
# state: sculk_sensor_phase, value_size: 3
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hab95f110453b7e5b8fedb47d53df8bbb9c409890 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf843c6db7ac59f63d5cb6df6ad3463914856a000 run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "sculk_sensor_phase"
function block:get_index with storage __st__ call
# state: waterlogged, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5fb89f95c7302b7ec4b5807b34c181a05c8085f5 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "waterlogged"
function block:get_index with storage __st__ call
