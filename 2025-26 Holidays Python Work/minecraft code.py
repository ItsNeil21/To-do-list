from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x, y, z = mc.player.TilePos()

for i in range(5)   :
    for j in range(5) :
        for k in range(5) :
            mc.setBlock(x + i, y + j, z + k, 1)