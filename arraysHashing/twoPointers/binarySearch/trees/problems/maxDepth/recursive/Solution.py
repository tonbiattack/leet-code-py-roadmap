# TreeNodeクラスの定義
from typing import Optional


class TreeNode:
    """
    二分探索木のノードを表すクラス。

    Attributes:
        val (int): ノードの値
        left (TreeNode): 左の子ノード（存在しない場合はNone）
        right (TreeNode): 右の子ノード（存在しない場合はNone）
    """

    def __init__(self, x):
        """
        TreeNodeの初期化。

        Args:
            x (int): ノードに格納する値
        """
        self.val = x  # ノードの値
        self.left = None  # 左の子ノードへの参照
        self.right = None  # 右の子ノードへの参照


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 呼び出し部分
if __name__ == "__main__":
    """
    手動で構築した二分探索木を用いて、最大の深さを計算します。

    ツリー構造:
        3
       / \
      9  20
        /  \
       15   7

    結果:
        このツリーの最大深さは3です。
    """
    root = TreeNode(3)  # ルートノード
    root.left = TreeNode(9)  # 左の子ノード
    root.right = TreeNode(20)  # 右の子ノード
    root.right.left = TreeNode(15)  # 右の子ノードの左
    root.right.right = TreeNode(7)  # 右の子ノードの右

    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # 最大深さを計算
    result = solution.maxDepth(root)

    # 結果を出力
    print("Maximum depth of the binary tree:", result)
