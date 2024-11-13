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


# なぜこの順序で探索するのか？
# このコードでは 中序順（in-order traversal） で二分探索木（Binary Search Tree; BST）を探索しています。中序順では「左ノード → 現在のノード → 右ノード」の順に探索するため、BSTの性質からノードの値が 昇順 に処理されるようになります。

# 中序順で探索する理由
# 昇順でノードを訪問:

# 二分探索木では、左の子ノードが現在のノードよりも小さく、右の子ノードが現在のノードよりも大きいという性質があります。
# 中序順で左→根→右と辿ることで、ノードを昇順に訪問できるため、各ノード間の最小差を効率よく計算できます。
# 最小差の計算:

# ノードが昇順で訪問されることで、現在のノードと前回のノード（隣接するノード）だけを比較すればよいことになります。これにより、効率的に最小差を求めることができます。
# 実行の流れ
# 最初に左の子ノードから順に進み、根ノードに戻り、その後右ノードに進むことで、ノードの値を昇順で取得します。
# これにより、隣接するノード間の差だけを比較すればよく、計算が効率化されます。
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 最小値を非常に大きな値で初期化
        self.minimum = float('inf')
        # 前回のノードの値を格納する変数
        self.prev = None

        # 深さ優先探索（中序順）を行う関数
        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            # 左の子ノードを再帰的に探索
            # 二分探索木（BST）では、左側のノードが現在のノードよりも小さい
            # 左側のノードを先に訪問することで、値を昇順に取得できる
            dfs(root.left)

            # 前のノードが存在する場合、差を計算して最小値を更新
            # 中序順では、ノードの値が昇順で訪問されるため、
            # 隣接するノード間の差を計算すれば、最小差を求めることができる
            if self.prev is not None:
                self.minimum = min(self.minimum, abs(root.val - self.prev))

            # 現在のノードの値を prev に更新
            # 次のノードと比較するために現在のノードの値を記憶する
            self.prev = root.val

            # 右の子ノードを再帰的に探索
            # 二分探索木では、右側のノードが現在のノードよりも大きい
            # 右側のノードを訪問することで、値を昇順のまま処理を進められる
            dfs(root.right)

        # dfs 関数を実行
        dfs(root)
        return self.minimum


# ノードを生成してツリー構造を作成
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Solutionインスタンスを生成して、getMinimumDifferenceを呼び出し
solution = Solution()
print(solution.getMinimumDifference(root))  # 結果は1が出力されるはずです
