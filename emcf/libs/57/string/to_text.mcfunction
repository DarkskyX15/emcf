setblock 0 319 0 minecraft:oak_sign
data modify block 0 319 0 front_text.messages[0] set value '{"type":"nbt","storage":"__st__","nbt":"register"}'
data modify storage __st__ call.m0 set from block 0 319 0 front_text.messages[0]
function string:_to_text/main with storage __st__ call
setblock 0 319 0 minecraft:air