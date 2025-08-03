# TreeNode クラスの定義
# TreeNodeは二分木の各ノードを表すクラスです。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値
        self.left = left  # 左部分木
        self.right = right  # 右部分木

# 問題「Binary Tree Tilt」は、二分木の「傾き (tilt)」を計算するものです。各ノードの「傾き」は、
# そのノードの左部分木の合計値と右部分木の合計値の差の絶対値として定義されます。木全体の「傾き」は、すべてのノードの「傾き」の合計です
class Solution:
    # findTilt メソッドは、与えられた二分木の「傾き」の合計を計算します。
    def findTilt(self, root: TreeNode) -> int:
        # 傾きの合計を保持する変数を用意
        self.total_tilt = 0

        # _sum_and_tilt はノードの部分木の合計と傾きを再帰的に計算します。
        def _sum_and_tilt(node: TreeNode) -> int:
            # 基本ケース: ノードが None の場合、部分木の合計は 0
            if not node:
                return 0

            # 左部分木の合計を再帰的に計算
            left_sum = _sum_and_tilt(node.left)

            # 右部分木の合計を再帰的に計算
            right_sum = _sum_and_tilt(node.right)

            # 現在のノードの「傾き」を計算（左部分木と右部分木の合計値の差の絶対値）
            tilt = abs(left_sum - right_sum)

            # 傾きの合計に現在のノードの傾きを加える
            self.total_tilt += tilt

            # 現在のノードをルートとする部分木の合計を返す
            return node.val + left_sum + right_sum

        # ルートノードから再帰を開始
        _sum_and_tilt(root)

        # 全体の傾きの合計を返す
        return self.total_tilt

# 以下は呼び出し箇所の例です。

# 例: 二分木の作成
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# ノードの作成
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

# Solution クラスのインスタンスを作成し、findTilt メソッドで木の「傾き」の合計を計算
solution = Solution()
print("木の傾きの合計:", solution.findTilt(root))  # 期待される出力は 9
