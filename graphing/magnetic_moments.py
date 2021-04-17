import matplotlib.pyplot as plt
import numpy as np
import math
import random

xy_length = math.sin(math.acos(math.sqrt(1/3)))
def vec(angle: float, is_up: bool):
    return [math.cos(angle)*xy_length, math.sin(angle)*xy_length, (is_up*2-1)*math.sqrt(1/3)]

axes = plt.figure().add_subplot(projection='3d')

vectors = [vec(random.uniform(0, math.tau), True) for x in range(20)] + [vec(random.uniform(0, math.tau), False) for x in range(10)]

xyz = np.zeros(len(vectors))
u, v, w = zip(*vectors)
axes.quiver(xyz, xyz, xyz, u, v, w, color=(1., 0.1, 0.5, 0.3))

axes.quiver(0, 0, 0, 0, 0, 1, color=(0, 0.5, 1))

axes.elev = 0
axes.grid(False)
axes.xaxis.set_pane_color((0, 0, 0, 0))
axes.yaxis.set_pane_color((0, 0, 0, 0))
axes.zaxis.set_pane_color((0, 0, 0, 0))
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
axes.set_xticks([])
axes.set_yticks([])
axes.set_zticks([])
axes.set_xlim([-xy_length, xy_length])
axes.set_ylim([-xy_length, xy_length])
axes.set_zlim([-math.sqrt(1/3), math.sqrt(1/3)])
plt.show()
