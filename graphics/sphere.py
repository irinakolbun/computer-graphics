from copy import copy
from graphics import Vector3, Camera
from graphics.object import Object
import numpy as np


class Sphere(Object):
    def __init__(self, pos: Vector3 = Vector3(), radius: np.float64 = 1):
        super().__init__()
        self._center = copy(pos)
        self._radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, x: Vector3):
        self._center = copy(x)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, x: np.float64):
        self._radius = x

    def ray_intersect(self, ray: Camera, epsilon=1e-6):
        L = ray.origin - self.center
        a = ray.direction * ray.direction
        b = ray.direction * L * 2
        c = L * L - self.radius

        roots = np.roots([a, b, c])

        res = []
        for root in roots:
            if root >= 0 and not np.iscomplex(root):
                res.append(ray.origin + ray.direction * root)

        return res
