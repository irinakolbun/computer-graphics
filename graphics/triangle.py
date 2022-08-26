from copy import copy
from graphics import Vector3, Camera
from graphics.object import Object
import numpy as np


class Triangle(Object):
    def __init__(self, v0: Vector3, v1: Vector3, v2: Vector3, n0: Vector3, n1: Vector3, n2: Vector3):
        super().__init__()
        self.v0 = copy(v0)
        self.v1 = copy(v1)
        self.v2 = copy(v2)
        self.n0 = copy(n0)
        self.n1 = copy(n1)
        self.n2 = copy(n2)

    def ray_intersect(self, ray: Camera, epsilon=1e-6):
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0

        pvec = ray.direction @ edge2
        det = edge1 * pvec

        # with culling
        if det < epsilon:
            return []

        tvec = ray.origin - self.v0
        u = tvec * pvec

        if u < 0 or u > det:
            return []

        qvec = tvec @ edge1

        v = ray.direction * qvec

        if v < 0 or u + v > det:
            return []

        t = edge2 * qvec
        inv_det = 1/det
        t *= inv_det
        u *= inv_det
        v *= inv_det

        return [[Vector3(t, u, v), (edge1 @ edge2).normalize()]]
