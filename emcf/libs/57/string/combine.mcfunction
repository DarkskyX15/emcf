setblock 0 319 0 minecraft:oak_sign
data modify block 0 319 0 front_text.messages[0] set value '{"type":"nbt","storage":"__st__","nbt":"call.m0"}'
data modify storage __st__ call.m0 set string block 0 319 0 front_text.messages[0] 1 -1
data modify block 0 319 0 front_text.messages[0] set value '{"type":"nbt","storage":"__st__","nbt":"call.m1"}'
data modify storage __st__ call.m1 set string block 0 319 0 front_text.messages[0] 1 -1
function string:_combine/main with storage __st__ call
setblock 0 319 0 minecraft:air