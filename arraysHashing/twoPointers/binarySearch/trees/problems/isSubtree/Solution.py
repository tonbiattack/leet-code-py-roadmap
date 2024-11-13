# TreeNodeクラスの定義
# 二分木のノードを表現するクラス
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

# Solutionクラスの定義
class Solution:
    # isSubtreeメソッド
    # s: 元の木の根ノード
    # t: 部分木であるかを確認する対象の木の根ノード
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # sがNoneの場合、部分木が存在しないためFalseを返す
        if not s:
            return False
        # isSameTreeメソッドを使って、sとtが同一の木かを確認
        if self.isSameTree(s, t):
            return True
        # 左右の子ノードに対して再帰的にisSubtreeを呼び出してチェック
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # isSameTreeメソッド
    # 二つの木が全く同じ構造と値を持っているかを確認する
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # pとqが共に存在する場合
        if p and q:
            # pとqの値が同じであり、さらに左右の子ノードも一致する場合にTrue
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # 片方がNoneで片方が存在する場合はFalse
        # 両方がNoneの場合はTrue
        return p is q

# ノードを生成してツリー構造を作成
# 元のツリーsの構築
p = TreeNode(1)
p.left = TreeNode(2)

# 部分木tの構築
q = TreeNode(1)
q.right = TreeNode(2)

# Solutionインスタンスを生成して、isSubtreeを呼び出し
solution = Solution()
print(solution.isSubtree(p, q))  # 出力はTrueまたはFalse
