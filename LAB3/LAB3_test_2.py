import unittest

from LAB3_2 import porazsort


class TestPorazsort(unittest.TestCase):

    def test_empt(self):
        self.assertEqual(porazsort([]), [])

    def test_one(self):
        self.assertEqual(porazsort([5]), [5])

    def test_sort(self):
        m = [10, 20, 30, 40, 50]
        self.assertEqual(porazsort(m), [10, 20, 30, 40, 50])

    def test_revsort(self):
        m = [50, 40, 30, 20, 10]
        self.assertEqual(porazsort(m), [10, 20, 30, 40, 50])

    def test_dubl(self):
        m = [30, 10, 20, 30, 10, 20]
        self.assertEqual(porazsort(m), [10, 10, 20, 20, 30, 30])

    def test_od(self):
        m = [111, 111, 111, 111]
        self.assertEqual(porazsort(m), [111, 111, 111, 111])

    def test_raz(self):
        m = [1, 200, 3, 40, 55, 700, 8, 90]
        expected = [1, 3, 8, 40, 55, 90, 200, 700]
        self.assertEqual(porazsort(m), expected)


if __name__ == '__main__':
    unittest.main()
