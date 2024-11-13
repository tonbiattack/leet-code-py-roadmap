# 問題の説明：
# 二分木が与えられたとき、その直径（ダイアメーター）を計算します。
# 二分木の直径とは、どの二つのノード間の最長パスのノード数から 1 を引いた値です。
# このパスは必ずしも根を通る必要はありません。

# 解説：
# - この問題では、二分木の中で最も長いパスの長さを求めます。
# - 再帰的な深さ優先探索（DFS）を使用して各ノードの左右の高さを計算し、
#   それらの合計が最大になるように更新します。
# - 各ノードで、左部分木と右部分木の高さの合計が、そのノードを通るパスの長さになります。
# - そのため、全てのノードでこの値を計算し、最大値を保持します。

# 必要なクラスの定義
from typing import Optional

# 二分木のノードを表すクラスを定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノードへの参照
        self.right = right  # 右の子ノードへの参照

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 結果を保存するためのインスタンス変数を初期化
        self.ans = 0

        # 深さ優先探索（DFS）のためのヘルパー関数を定義
        def dfs(node: Optional[TreeNode]) -> int:
            # ベースケース：ノードが存在しない場合、高さは 0
            if not node:
                return 0

            # 左部分木の高さを再帰的に計算
            left = dfs(node.left)
            # 右部分木の高さを再帰的に計算
            right = dfs(node.right)

            # 現在のノードを通るパスの長さを計算し、最大値を更新
            self.ans = max(self.ans, left + right)

            # デバッグ用出力（必要に応じてコメントアウト）
            # print(f"ノード値: {node.val}, 左高さ: {left}, 右高さ: {right}, 現在の最大直径: {self.ans}")

            # 現在のノードの高さを返す
            return max(left, right) + 1

        # 再帰的な探索を開始
        dfs(root)

        # 最終的な直径の値を返す
        return self.ans

def main():
    # 二分木を構築するための例を作成
    # 例として以下の二分木を考えます：
    #         1
    #        / \
    #       2   3
    #      / \     
    #     4   5

    # ノードを作成
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    # ノードを接続して二分木を構築
    node1.left = node2    # 1 の左子を 2 に設定
    node1.right = node3   # 1 の右子を 3 に設定
    node2.left = node4    # 2 の左子を 4 に設定
    node2.right = node5   # 2 の右子を 5 に設定

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # メソッドを呼び出して二分木の直径を計算
    diameter = solution.diameterOfBinaryTree(node1)

    # 結果を出力
    print("二分木の直径は:", diameter)

if __name__ == "__main__":
    main()
