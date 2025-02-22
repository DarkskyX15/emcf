# states index: 65
data modify storage __st__ call.m2 set value "65"
# state: age, value_size: 26
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/h6d09caaf473fececb51105ff136dd1ce172d7b39 run scoreboard players add __gen__ __bd__ 1
execute if predicate __nsp__:bp/sub/hf29bddcb78bc7eb653cf4cc81b76d4b357125835 run scoreboard players add __gen__ __bd__ 2
execute if predicate __nsp__:bp/sub/ha6c63b22d27efea2f8afc8a2fa6846e96a971777 run scoreboard players add __gen__ __bd__ 4
execute if predicate __nsp__:bp/sub/h5dc303348044a1665a5ffffc264968974070adfe run scoreboard players add __gen__ __bd__ 8
execute if predicate __nsp__:bp/sub/h5e3bbf527cb2c740cd02e657e419cd35d128ea8d run scoreboard players add __gen__ __bd__ 16
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "age"
function block:get_index with storage __st__ call
# state: berries, value_size: 2
scoreboard players set __gen__ __bd__ 0
execute if predicate __nsp__:bp/sub/hc227701940e2450c82f27046d4a6ea51c647ac86 run scoreboard players add __gen__ __bd__ 1
execute store result storage __st__ call.m0 int 1.0 run scoreboard players get __gen__ __bd__
data modify storage __st__ call.m1 set value "berries"
function block:get_index with storage __st__ call
