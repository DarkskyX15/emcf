setblock 0 319 0 minecraft:oak_sign
data modify block 0 319 0 front_text.messages[0] set value '{"type":"nbt","storage":"__st__","nbt":"call.m1"}'
data modify storage __st__ call.m1 set string block 0 319 0 front_text.messages[0] 1 -1
setblock 0 319 0 minecraft:air