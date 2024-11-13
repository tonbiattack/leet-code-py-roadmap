# TreeNodeクラスを定義
# 各ノードには値(val)、左(left)と右(right)の子ノードを持つ
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

from typing import Optional  # Optionalは型ヒントのために使う

# Solutionクラスを定義し、isBalancedメソッドを作成
class Solution:
    # 二分木が平衡かどうかを確認するメソッド
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 深さ優先探索（DFS）を行う内部関数を定義
        def dfs(root):
            # ベースケース: ノードがない場合は木の高さは0であり、平衡であると見なす
            if not root:
                return [True, 0]  # [木が平衡であるか, 高さ]

            # 左右のサブツリーをそれぞれ再帰的に探索
            left, right = dfs(root.left), dfs(root.right)

            # 平衡条件の確認:
            # 左右のサブツリーがそれぞれ平衡であり、かつ高さの差が1以内
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # 現在のノードを含む木の高さは、左右の高さの最大値+1
            return [balanced, 1 + max(left[1], right[1])]

        # ルートノードから開始し、結果を返す（木が平衡かどうかの判定を返す）
        return dfs(root)[0]

# 呼び出し側のコード
# ツリーノードを作成して平衡かどうか確認する
if __name__ == "__main__":
    # サンプルの二分木を作成
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Solutionクラスのインスタンスを作成
    solution = Solution()
    # isBalancedメソッドを呼び出し、木が平衡かどうかを判定
    result = solution.isBalanced(root)
    print("Balanced" if result else "Not Balanced")  # 結果を出力
