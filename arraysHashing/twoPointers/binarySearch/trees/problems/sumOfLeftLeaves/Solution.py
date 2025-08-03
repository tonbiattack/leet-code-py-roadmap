# TreeNodeクラスの定義
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        # 深さ優先探索の定義
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            # 左の子ノードが存在し、かつ左の子ノードが葉である場合
            if node.left and not node.left.left and not node.left.right:
                self.sum += node.left.val
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        return self.sum


# 呼び出し箇所
if __name__ == "__main__":
    # 木構造の構築
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # hasPathSumメソッドの呼び出し
    print(sol.sumOfLeftLeaves(root))
