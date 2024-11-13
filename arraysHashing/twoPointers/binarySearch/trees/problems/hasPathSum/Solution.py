# TreeNodeクラスの定義
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solutionクラスの定義


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # ノードが存在しない場合はFalse
        if not root:
            return False

        # リーフノード（子ノードが無いノード）に到達した場合、targetSumとノードの値を比較
        if not root.left and not root.right:
            return targetSum == root.val

        # 左部分木での再帰的なチェック
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        # 右部分木での再帰的なチェック
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        # 左か右のどちらかで合計が一致すればTrueを返す
        return left_sum or right_sum


# 呼び出し箇所
if __name__ == "__main__":
    # 木構造の構築
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # hasPathSumメソッドの呼び出し
    target_sum = 22
    result = sol.hasPathSum(root, target_sum)

    # 結果の出力
    print(f"Has path sum of {target_sum}? {result}")
