import numpy as np
from graphics import *
from PIL import Image
from multiprocessing import Pool

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    scene = Scene(100, 100, 50)

    pool = Pool(8)

    obj = open('obj/cow.obj')

    v, vn = [], []

    for line in obj:
        if line.startswith('v '):
            v.append(Vector3(*map(np.float64, line.split(' ')[1:])))
        if line.startswith('vn '):
            vn.append(Vector3(*map(np.float64, line.split(' ')[1:])))
        if line.startswith('f '):
            a, b, c = line.split(' ')[1:]
            v0, n0 = map(int, (a.split('//')))
            v1, n1 = map(int, (b.split('//')))
            v2, n2 = map(int, (c.split('//')))
            v0, v1, v2 = v[v0-1], v[v1-1], v[v2-1]
            n0, n1, n2 = vn[n0-1], vn[n1-1], vn[n2-1]

            scene.add_object(Triangle(v0, v1, v2, n0, n1, n2))

    # frame = scene.render()
    frame = scene.render_mp(pool)

    # print(frame)

    # img = Image.fromarray(np.uint8(frame * 255), 'L')
    img = Image.fromarray(frame, mode="RGB")
    img.show()


