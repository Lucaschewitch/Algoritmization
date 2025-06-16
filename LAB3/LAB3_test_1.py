import unittest
from LAB3_1 import sliyaniye


class TestSliyaniye(unittest.TestCase):
    def test_empt(self):
        m = []
        sliyaniye(m)
        self.assertEqual(m, [])

    def test_one(self):
        m = [42]
        sliyaniye(m)
        self.assertEqual(m, [42])

    def test_sort(self):
        m = [1, 2, 3, 4, 5]
        sliyaniye(m)
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_revsort(self):
        m = [10, 8, 6, 4, 2]
        sliyaniye(m)
        self.assertEqual(m, [2, 4, 6, 8, 10])

    def test_dubl(self):
        m = [5, 3, 5, 2, 3, 2]
        sliyaniye(m)
        self.assertEqual(m, [2, 2, 3, 3, 5, 5])

    def test_nec(self):
        m = [38, 27, 43, 3, 9, 82, 10]
        sliyaniye(m)
        self.assertEqual(m, [3, 9, 10, 27, 38, 43, 82])

    def test_c(self):
        m = [4, -2, 0, 8, 1, -5]
        sliyaniye(m)
        self.assertEqual(m, [-5, -2, 0, 1, 4, 8])


if __name__ == "__main__":
    unittest.main()
