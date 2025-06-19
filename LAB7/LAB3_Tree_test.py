import unittest
from LAB7_Tree import twin
from LAB7_Tree import TreeNode


class TestTwinFunction(unittest.TestCase):
    def test_2emp(self):
        # оба пустые
        self.assertTrue(twin(None, None))

    def test_1emp(self):
        # пустое и нет
        non_empty = TreeNode(1)
        self.assertFalse(twin(None, non_empty))
        self.assertFalse(twin(non_empty, None))

    def test_eq(self):
        # одинаковые
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(2)
        tree2.right = TreeNode(3)

        self.assertTrue(twin(tree1, tree2))

    def test_almeq(self):
        # разные листочки
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(4)
        tree2.right = TreeNode(3)

        self.assertFalse(twin(tree1, tree2))

    def test_timofey(self):
        # Тимофеевы близнецы
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(3)
        tree2.right = TreeNode(2)

        self.assertFalse(twin(tree1, tree2))

    def test_noneq(self):
        # вообще разные деревья жестб
        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)

        tree2 = TreeNode(10)
        tree2.left = TreeNode(20)
        tree2.right = TreeNode(30)

        self.assertFalse(twin(tree1, tree2))


if __name__ == '__main__':
    unittest.main()
