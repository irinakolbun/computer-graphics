import numpy as np
from graphics.matrix import Matrix44f

translation = (np.array(((1, 0, 0, 0),      # (1, 0, 0, tx)
                         (0, 1, 0, 0),      # (0, 1, 0, ty)
                         (0, 0, 1, 0),      # (0, 0, 1, tz)
                         (0, 0, 0, 1))))    # (0, 0, 0, 1)

scale = (np.array(((1, 0, 0, 0),            # (sx, 0, 0, 0)
                   (0, 1, 0, 0),            # (0, sy, 0, 0)
                   (0, 0, 1, 0),            # (0, 0, sz, 0)
                   (0, 0, 0, 1))))          # (0, 0, 0, 1)

rotation_x = (np.array(((1, 0, 0, 0),       # (1, 0, 0, 0,)
                        (0, -0.7, -0.7, 0),       # (0, cos, sin, 0)
                        (0, 0.7, -0.7, 0),       # (0, -sin, cos, 0)
                        (0, 0, 0, 1))))     # (0, 0, 0, 1)

rotation_y = (np.array(((0.7, 0, -0.7, 0),       # (cos, 0, -sin, 0)
                        (0, 1, 0, 0),       # (0, 1, 0, 0)
                        (0.7, 0, 0.7, 0),       # (sin, 0, cos, 0)
                        (0, 0, 0, 1))))     # (0, 0, 0, 1)

rotation_z = (np.array(((1, 0, 0, 0),       # (cos, -sin, 0, 0)
                        (0, 1, 0, 0),       # (sin, cos, 0, 0)
                        (0, 0, 1, 0),       # (0, 0, 1, 0)
                        (0, 0, 0, 1))))     # (0, 0, 0, 1)

rotation = np.matmul(np.matmul(rotation_x, rotation_y), rotation_z)

transformation = Matrix44f(np.matmul(np.matmul(translation, rotation), scale))

# print(transformation)
