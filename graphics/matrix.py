import numpy as np

from graphics import Vector3


class Matrix44f:
    def __init__(self, matrix: np.ndarray):
        self._matrix = matrix.copy()

    def mult_dir_matrix(self, n: Vector3):
        m = self._matrix
        return Vector3(n.x * m[0][0] + n.y * m[1][0] + n.z * m[2][0],
                       n.x * m[0][1] + n.y * m[1][1] + n.z * m[2][1],
                       n.x * m[0][2] + n.y * m[1][2] + n.z * m[2][2])

    def mult_vec_matrix(self, n: Vector3):
        m = self._matrix

        a = n.x * m[0][0] + n.y * m[1][0] + n.z * m[2][0] + m[3][0]
        b = n.x * m[0][1] + n.y * m[1][1] + n.z * m[2][1] + m[3][1]
        c = n.x * m[0][2] + n.y * m[1][2] + n.z * m[2][2] + m[3][2]
        w = n.x * m[0][3] + n.y * m[1][3] + n.z * m[2][3] + m[3][3]

        return Vector3(a/w, b/w, c/w)
