# TreeNodeクラスの定義
from typing import Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 値を格納するセットを初期化
        self.seen_values = set()

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            # k - node.val が seen_values に存在する場合、2つの値の和が k になる
            if (k - node.val) in self.seen_values:
                return True

            # 現在のノードの値をセットに追加
            self.seen_values.add(node.val)

            # 左右の部分木を再帰的に探索
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

# 呼び出し箇所
if __name__ == "__main__":
    # 木構造の構築
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # findTargetメソッドの呼び出し
    print(sol.findTarget(root, 9))  # 期待される出力は True（5 + 4 = 9）
    print(sol.findTarget(root, 3))  # 期待される出力は False
