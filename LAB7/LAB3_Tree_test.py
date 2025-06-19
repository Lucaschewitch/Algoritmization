import unittest
from LAB7_Tree import twin
from LAB7_Tree import TreeNode


class TestTwinFunction(unittest.TestCase):
    def test_2emp(self):
        # оба пустые
        self.assertTrue(twin(None, None))

    def test_1emp(self):
        # пустое и нет
        ne = TreeNode(1)
        self.assertFalse(twin(None, ne))
        self.assertFalse(twin(ne, None))

    def test_eq(self):
        # одинаковые
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)

        t2 = TreeNode(1)
        t2.left = TreeNode(2)
        t2.right = TreeNode(3)

        self.assertTrue(twin(t1, t2))

    def test_almeq(self):
        # разные листочки
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)

        t2 = TreeNode(1)
        t2.left = TreeNode(4)
        t2.right = TreeNode(3)

        self.assertFalse(twin(t1, t2))

    def test_timofey(self):
        # Тимофеевы близнецы
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)

        t2 = TreeNode(1)
        t2.left = TreeNode(3)
        t2.right = TreeNode(2)

        self.assertFalse(twin(t1, t2))

    def test_noneq(self):
        # вообще разные деревья жестб
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)

        t2 = TreeNode(10)
        t2.left = TreeNode(20)
        t2.right = TreeNode(30)

        self.assertFalse(twin(t1, t2))


if __name__ == '__main__':
    unittest.main()
