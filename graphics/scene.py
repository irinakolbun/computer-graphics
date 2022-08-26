import numpy as np

import graphics.transformation
from graphics import Camera, Vector3
from graphics.matrix import Matrix44f
from graphics.object import Object


class Scene:
    def __init__(self, width=50, height=50, fov=70):
        self._objects = []
        self._camera = Camera(Vector3(0, 0, -1.2), Vector3(0, 1, 0))
        self._width = width
        self._height = height
        self._fov = fov
        # self._fb = np.zeros((width, height), np.float64)
        self._fb = np.zeros((width, height, 3), dtype=np.uint8)
        self._scale = np.tan(np.deg2rad(self._fov * 0.5))
        self._aspect_ratio = np.float64(self._width) / np.float64(self._height)
        # self._camera_to_world = Matrix44f(np.array(((1, 0, 0, 0),
        #                                             (0, 0, 1, 0),
        #                                             (0, 1, -1, 0),
        #                                             (0, 0, 0, 1))))
        self._camera_to_world = graphics.transformation.transformation
        self._light_source = Vector3(0, 1, 1).normalize()

    def add_object(self, obj: Object):
        self._objects.append(obj)

    def cast_ray(self, camera):
        min_dist, res = np.finfo(np.float64).max, None
        intersections = [x.ray_intersect(camera) for x in self._objects]
        flat_int = [x for sub in intersections for x in sub]
        for intersection in flat_int:
            if abs(camera.origin - intersection[0]) < min_dist:
                min_dist = abs(camera.origin - intersection[0])
                res = intersection
                # [
                #     [[Vector3(), Vector3()], [Vector3(), Vector3()]],
                #     [[Vector3(), Vector3()]],
                #     []
                #  ]
                # ->
                # [Vector3(), Vector3()], [Vector3(), Vector3()], [Vector3(), Vector3()], []

        if res is not None:
            shadow = 0.5 if [obj.ray_intersect(Camera(res[0], (self._light_source - res[0]).normalize())) for obj in self._objects] else 1
            normal_color = ((Vector3(1, 1, 1) + res[1])*0.5)*255
            return (normal_color * shadow * (self._light_source * res[1])).as_array() if self._light_source * res[1] > 0 else [0, 0, 0]
        else:
            return [0x67, 0xB7, 0xD1]

    def render(self):
        origin = self._camera_to_world.mult_vec_matrix(self._camera.origin)
        for j in range(self._height):
            for i in range(self._width):
                x = (2 * (i + 0.5) / np.float64(self._width) - 1) * self._aspect_ratio * self._scale
                y = (1 - 2 * (j + 0.5) / np.float64(self._height)) * self._scale
                direction = self._camera_to_world.mult_dir_matrix(Vector3(x, y, -1))
                direction = direction.normalize()
                ray_casted = self.cast_ray(Camera(origin, direction))
                self._fb[i][j] = ray_casted
        return self._fb.copy()

    def render_mp_helper(self, camera):
        return self.cast_ray(camera)

    def render_mp(self, pool):
        to_process = []
        for j in range(self._height):
            for i in range(self._width):
                origin = self._camera_to_world.mult_vec_matrix(self._camera.origin)
                x = (2 * (i + 0.5) / np.float64(self._width) - 1) * self._aspect_ratio * self._scale
                y = (1 - 2 * (j + 0.5) / np.float64(self._height)) * self._scale
                direction = self._camera_to_world.mult_dir_matrix(Vector3(x, y, -1))
                direction = direction.normalize()
                to_process.append(Camera(origin, direction))

        results = pool.map(self.render_mp_helper, to_process, chunksize=200)

        for j in range(self._height):
            for i in range(self._width):
                self._fb[i][j] = results[j*self._height+i]
        return self._fb.copy()
