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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# ノードを生成してツリー構造を作成
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Solutionインスタンスを生成して、countNodesを呼び出し
solution = Solution()
print(solution.invertTree(root))  # 結果は7が出力されるはずです
