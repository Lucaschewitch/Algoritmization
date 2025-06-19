class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def twin(p, q):
    # оба узла пусты (если дошло до этого)
    if p is None and q is None:
        return True

    # если одно дерево больше другого
    if p is None or q is None:
        return False

    # разные значения
    if p.val != q.val:
        return False
    # and чтобы выполнялись для всех ветвей
    return twin(p.left, q.left) and twin(p.right, q.right)


if __name__ == "__main__":
    # A:           1
    #             / \
    #            2   3
    ta = TreeNode(1)
    ta.left = TreeNode(2)
    ta.right = TreeNode(3)

    # B:        1
    #          / \
    #         2   3
    tb = TreeNode(1)
    tb.left = TreeNode(2)
    tb.right = TreeNode(3)

    #  C:    1
    #       / \
    #      3   2
    tc = TreeNode(1)
    tc.left = TreeNode(3)
    tc.right = TreeNode(2)

    # D:        1
    #          / \
    #         2   4
    td = TreeNode(1)
    td.left = TreeNode(2)
    td.right = TreeNode(4)

    print("A и B близнецы:", twin(ta, tb))
    print("A и C близнецы:", twin(ta, tc))
    print("A и D близнецы:", twin(ta, td))
