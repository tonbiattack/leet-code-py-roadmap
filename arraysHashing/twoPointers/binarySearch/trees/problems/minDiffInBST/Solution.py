# TreeNodeクラスの定義
from typing import Optional

# TreeNode クラスは、二分探索木のノードを表します。
# ここでは、val にノードの値を持ち、left と right に左子ノードと右子ノードへの参照を持ちます。


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

# Solution クラスには、minDiffInBST メソッドが含まれ、二分探索木での最小差を計算します。


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # ans は最小の差を保存する変数で、最初は無限大で初期化します
        self.ans = float('inf')

        # pred は、直前のノードの値を保存するための変数です
        self.pred = None

        # 中順 (inorder) でツリーを巡回します
        self.inorder(root)

        # 最終的な最小差を返します
        return self.ans

    # inorder メソッドは中順でツリーを巡回し、最小の差を計算します
    def inorder(self, root: TreeNode) -> None:
        # ベースケース：ノードが None の場合、再帰を終了します
        if root is None:
            return

        # 左の子ノードを巡回します（再帰的に呼び出し）
        self.inorder(root.left)

        # pred が None でない場合、現在のノードの値と pred の差を計算します
        if self.pred is not None:
            # ans は、現在の ans と pred との差の最小値に更新されます
            self.ans = min(self.ans, root.val - self.pred)

        # 現在のノードの値を pred に設定します
        self.pred = root.val

        # 右の子ノードを巡回します（再帰的に呼び出し）
        self.inorder(root.right)


# 呼び出し箇所
if __name__ == "__main__":
    # 木構造の構築
    # 以下のように二分探索木を構築します
    #     1
    #      \
    #       2
    #      /
    #     3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    # Solution クラスのインスタンスを作成し、minDiffInBST メソッドを呼び出します
    sol = Solution()
    print(sol.minDiffInBST(root))  # 最小の差を出力します
