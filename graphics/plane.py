from copy import copy
from graphics import Vector3, Camera
from graphics.object import Object


class Plane(Object):
    def __init__(self, normal: Vector3 = Vector3(), pos: Vector3 = Vector3()):
        super().__init__()
        self._normal = copy(normal)
        self._position = copy(pos)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, x: Vector3):
        self._position = copy(x)

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, x: Vector3):
        self._normal = copy(x)

    def ray_intersect(self, ray: Camera, epsilon=1e-6):
        ndotu = self.normal * ray.direction
        if abs(ndotu) < epsilon:
            return []

        w = ray.origin - self.position
        si = (-self.normal * w) / ndotu
        Psi = w + ray.direction * si + self.position
        return [Psi]

