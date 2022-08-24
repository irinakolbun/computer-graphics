from copy import copy
from graphics import Vector3, Ray
import numpy as np


class Camera(Ray):
    def __init__(self, origin: Vector3 = Vector3(), dir: Vector3 = Vector3()):
        super().__init__()
        self._origin = copy(origin)
        self._direction = copy(dir)

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, x: Vector3):
        self._origin = copy(x)

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, x: Vector3):
        self._direction = copy(x)
