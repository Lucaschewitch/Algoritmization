import unittest
from LAB7_BackT import norm, bt


class TestGraphColoring(unittest.TestCase):
    def test_norm_nonconf(self):
        m = [['0', '1'], ['1', '0']]
        cs = [0, 0]
        self.assertTrue(norm(0, 1, m, cs))

    def test_norm_conf(self):
        m = [['0', '1'], ['1', '0']]
        cs = [0, 1]
        self.assertFalse(norm(0, 1, m, cs))

    def test_norm_nonsosed(self):
        m = [['0', '0'], ['0', '0']]
        cs = [0, 0]
        self.assertTrue(norm(0, 1, m, cs))

    def test_bt_norm(self):
        m = [['0', '1'], ['1', '0']]
        n = 2
        k = 2
        cs = [0] * n
        self.assertTrue(bt(0, cs, m, n, k))
        self.assertNotEqual(cs[0], cs[1])

    def test_bt_nenorm(self):
        m = [['0', '1'], ['1', '0']]
        n = 2
        k = 1
        cs = [0] * n
        self.assertFalse(bt(0, cs, m, n, k))

    def test_bt_nenormtr(self):
        m = [
            ['0', '1', '1'],
            ['1', '0', '1'],
            ['1', '1', '0']
        ]
        n = 3
        k = 2
        cs = [0] * n
        self.assertFalse(bt(0, cs, m, n, k))

    def test_bt_normtr(self):
        m = [
            ['0', '1', '1'],
            ['1', '0', '1'],
            ['1', '1', '0']
        ]
        n = 3
        k = 3
        cs = [0] * n
        self.assertTrue(bt(0, cs, m, n, k))
        self.assertTrue(all(cs))
        self.assertNotEqual(cs[0], cs[1])
        self.assertNotEqual(cs[0], cs[2])
        self.assertNotEqual(cs[1], cs[2])


if __name__ == '__main__':
    unittest.main()
