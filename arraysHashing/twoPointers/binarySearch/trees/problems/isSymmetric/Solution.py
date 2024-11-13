# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    # TreeNodeクラスのコンストラクタ
    # val: ノードの値（デフォルト0）
    # left: 左の子ノード（デフォルトNone）
    # right: 右の子ノード（デフォルトNone）
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(n1, n2):  # n1:left, n2:right
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

        return is_mirror(root.left, root.right)


# ノードを生成してツリー構造を作成
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right.right = TreeNode(3)
p.right.left = TreeNode(4)


# Solutionインスタンスを生成して、countNodesを呼び出し
solution = Solution()
print(solution.isSymmetric(p))  # 結果は7が出力されるはずです
