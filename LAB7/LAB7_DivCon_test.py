import unittest
from LAB7_DivCon import ff, fl, ffl


class TestBinarySearch(unittest.TestCase):
    def test_ed(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ff(arr, 3), 2)
        self.assertEqual(fl(arr, 3), 2)
        self.assertEqual(ffl(arr, 3), (2, 2))

    def test_mnogo(self):
        arr = [1, 2, 3, 3, 3, 4, 5]
        self.assertEqual(ff(arr, 3), 2)
        self.assertEqual(fl(arr, 3), 4)
        self.assertEqual(ffl(arr, 3), (2, 4))

    def test_noel(self):
        arr = [1, 2, 4, 5]
        self.assertEqual(ff(arr, 3), -1)
        self.assertEqual(fl(arr, 3), -1)
        self.assertEqual(ffl(arr, 3), -1)

    def test_emp(self):
        arr = []
        self.assertEqual(ff(arr, 3), -1)
        self.assertEqual(fl(arr, 3), -1)
        self.assertEqual(ffl(arr, 3), -1)

    def test_el(self):
        arr = [1, 2, 2, 3, 4, 4]
        # Первый элемент
        self.assertEqual(ff(arr, 1), 0)
        self.assertEqual(fl(arr, 1), 0)
        # Последний элемент
        self.assertEqual(ff(arr, 4), 4)
        self.assertEqual(fl(arr, 4), 5)
        # Левый край (множественные вхождения)
        self.assertEqual(ff(arr, 2), 1)
        self.assertEqual(fl(arr, 2), 2)

    def test_odin(self):
        arr = [5, 5, 5, 5]
        self.assertEqual(ff(arr, 5), 0)
        self.assertEqual(fl(arr, 5), 3)
        self.assertEqual(ffl(arr, 5), (0, 3))


if __name__ == "__main__":
    unittest.main()
