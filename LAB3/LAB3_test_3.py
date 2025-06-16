import unittest
from LAB3_3 import bsort


class TestBubbleSort(unittest.TestCase):
    def test_emp(self):
        self.assertEqual(bsort([]), [])

    def test_one(self):
        self.assertEqual(bsort([7]), [7])

    def test_sort(self):
        self.assertEqual(bsort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_revsort(self):
        self.assertEqual(bsort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_dubl(self):
        self.assertEqual(bsort([5, 3, 5, 3, 2]), [2, 3, 3, 5, 5])

    def test_nesort(self):
        self.assertEqual(bsort([3, 6, 8, 10, 1, 2, 12]), [1, 2, 3, 6, 8, 10, 12])

    def test_neorig(self):
        arr = [3, 1, 2]
        bsort(arr)
        self.assertEqual(arr, [3, 1, 2])


if __name__ == '__main__':
    unittest.main()
