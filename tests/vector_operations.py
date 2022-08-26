import unittest
from graphics.vector import Vector3


class VectorOperations(unittest.TestCase):
    def test_vec_sum(self):
        self.assertEqual(Vector3(5, 2, 1) + Vector3(1, 1, 1), Vector3(5 + 1, 2 + 1, 1 + 1))

    def test_vec_abs(self):
        vec = Vector3(3, 4, 5)
        length = round(abs(vec), 2)
        self.assertEqual(length, 7.07)


if __name__ == '__main__':
    unittest.main()
