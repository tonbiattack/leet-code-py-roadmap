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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



# ノードを生成してツリー構造を作成
# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(3)
# q = TreeNode(1)
# q.left = TreeNode(2)
# q.right = TreeNode(3)
p = TreeNode(1)
p.left = TreeNode(2)
# p.right = TreeNode(3)
q = TreeNode(1)
# q.left = TreeNode(2)
q.right = TreeNode(2)
# root.right.right = TreeNode(7)

# Solutionインスタンスを生成して、countNodesを呼び出し
solution = Solution()
print(solution.isSameTree(p, q))  # 結果は7が出力されるはずです
