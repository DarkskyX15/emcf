# states index: 117
data modify storage __st__ call.m2 set value "117"
# state: facing, value_size: 4
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h5ea33a3a73350bf262f3f7ab54c719df93c996ba run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/he870825c268ff6208dc22fb08aeb7e91de067edf run scoreboard players add __gen__ __bd__ 2
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "facing"
function block:get_index with storage __st__ call
# state: slot_0_occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h940fbcd0ac0587896645f38ebcabef96d7c40ac0 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "slot_0_occupied"
function block:get_index with storage __st__ call
# state: slot_1_occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hfc39d5e4fa7ea00b674d559c9125e544e51344d8 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "slot_1_occupied"
function block:get_index with storage __st__ call
# state: slot_2_occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h8b529bb2325b8326bf13f7da451cbb6dd72dd96f run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "slot_2_occupied"
function block:get_index with storage __st__ call
# state: slot_3_occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h062ec661476f4b0ebe707193749e84117902c744 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "slot_3_occupied"
function block:get_index with storage __st__ call
# state: slot_4_occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hab87730a6595cc647084a453f9ca08ddcbf38c39 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "slot_4_occupied"
function block:get_index with storage __st__ call
# state: slot_5_occupied, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hacc18f7c496f93b0839502f3b5d2a938b068c3fa run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "slot_5_occupied"
function block:get_index with storage __st__ call
