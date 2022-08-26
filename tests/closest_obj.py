import unittest

import numpy
import numpy as np
from PIL import Image

from graphics import Scene, Camera, Vector3, Sphere
from graphics.matrix import Matrix44f


class MyTestCase(unittest.TestCase):
    def test_closest(self):
        scene = Scene(100, 100, 50)
        scene._camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0))
        scene._camera_to_world = Matrix44f(np.array(((1, 0, 0, 0),
                                                     (0, 1, 0, 0),
                                                     (0, 0, 1, 0),
                                                     (0, 0, 0, 1))))


        scene.add_object(Sphere(Vector3(0, 0, -2), 0.2))

        frame1 = scene.render()

        scene.add_object(Sphere(Vector3(0, 0, -4), 0.1))

        frame2 = scene.render()

        img = Image.fromarray(frame1, mode="RGB")
        img.show()
        img = Image.fromarray(frame2, mode="RGB")
        img.show()

        self.assert_(numpy.allclose(frame1, frame2))


if __name__ == '__main__':
    unittest.main()
