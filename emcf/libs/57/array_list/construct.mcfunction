data modify storage __st__ register set value {v:0}
data modify storage __st__ cache.result set value []
scoreboard players set __gen__ __bd__ 0
execute store result score __cst__ __bd__ run data get storage __st__ cache.src
function al_ops:_construct/main