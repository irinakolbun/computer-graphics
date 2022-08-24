import numpy as np
from graphics import *
from PIL import Image

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    scene = Scene(100, 100)
    scene.add_object(Sphere(Vector3(0, 0, -20), 0.1))
    scene.add_object(Sphere(Vector3(0, -1, -2), 0.1))
    scene.add_object(Sphere(Vector3(0, 1, -2), 0.1))
    # scene.add_object(Sphere(Vector3(0, 1.5, -3.5), 0.2))
    # scene.add_object(Sphere(Vector3(0, -1.5, -3.5), 0.2))
    # scene.add_object(Sphere(Vector3(1.5, -1.5, -3.5), 0.2))
    frame = scene.render()

    img = Image.fromarray(np.uint8(frame * 255), 'L')
    img.show()
