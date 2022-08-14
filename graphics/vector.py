import numpy as np


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self._x = np.float64(x)
        self._y = np.float64(y)
        self._z = np.float64(z)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, x):
        self._x = np.float64(x)

    @y.setter
    def y(self, y):
        self._y = np.float64(y)

    @z.setter
    def z(self, z):
        self._z = np.float64(z)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f'(x={self.x}, y={self.y}, z={self.z})'

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return Vector3(self.x, self.y, self.z)

    def __neg__(self):
        # noinspection PyTypeChecker
        return Vector3(-self.x, -self.y, -self.z)

    def __truediv__(self, other: np.float64):
        # noinspection PyTypeChecker
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __abs__(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __mul__(self, other):
        """
        Dot product
        :param other: other vector
        :return: float: scalar
        """
        if type(other) is Vector3:
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vector3(self.x * other, self.y * other, self.z * other)

    def __matmul__(self, other):
        """
        Cross product
        :param other: other vector
        :return: Vector3
        """
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def normalize(self):
        return self / abs(self)
