execute if score __dist__ __bd__ matches 0 run return run scoreboard players set __dist3__ __bd__ 0
scoreboard players set __dist3__ __bd__ 9
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 10
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 100
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 1000
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 10000
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 100000
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 1000000
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 10000000
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1
scoreboard players operation __dist4__ __bd__ = __dist__ __bd__
scoreboard players set __cst__ __bd__ 100000000
scoreboard players operation __dist4__ __bd__ %= __cst__ __bd__
execute unless score __dist4__ __bd__ matches 0 run return 1
scoreboard players remove __dist3__ __bd__ 1