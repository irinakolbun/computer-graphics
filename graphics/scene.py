import numpy as np

from graphics import Camera, Vector3
from graphics.matrix import Matrix44f
from graphics.object import Object


class Scene:
    def __init__(self, width=50, height=50, fov=70):
        self._objects = []
        self._camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0))
        self._width = width
        self._height = height
        self._fov = fov
        self._fb = np.zeros((width, height), np.float64)
        self._scale = np.tan(np.deg2rad(self._fov * 0.5))
        self._aspect_ratio = np.float64(self._width) / np.float64(self._height)
        self._camera_to_world = Matrix44f(np.array(((1, 0, 0, 0),
                                                    (0, 1, 0, 0),
                                                    (0, 0, 1, 0),
                                                    (0, 0, 0, 1))))
        self._light_source = Vector3(0, 1, 1).normalize()

    def add_object(self, obj: Object):
        self._objects.append(obj)

    def cast_ray(self, camera):
        min_dist, res = np.finfo(np.float64).max, None
        intersections = [x.ray_intersect(camera) for x in self._objects]
        flat_int = [x for sub in intersections for x in sub]
        for intersection in flat_int:
            if abs(intersection[0]) < min_dist:
                min_dist = abs(intersection[0])
                res = intersection

        if res is not None:
            # return 1
            return self._light_source * res[1] if self._light_source * res[1] > 0 else 0
        else:
            return 0

    def render(self):
        origin = self._camera_to_world.mult_vec_matrix(self._camera.origin)
        for j in range(self._height):
            for i in range(self._width):
                x = (2 * (i + 0.5) / np.float64(self._width) - 1) * self._aspect_ratio * self._scale
                y = (1 - 2 * (j + 0.5) / np.float64(self._height)) * self._scale
                direction = self._camera_to_world.mult_dir_matrix(Vector3(x, y, -1))
                direction = direction.normalize()
                self._fb[i][j] = self.cast_ray(Camera(origin, direction))
        return self._fb.copy()
