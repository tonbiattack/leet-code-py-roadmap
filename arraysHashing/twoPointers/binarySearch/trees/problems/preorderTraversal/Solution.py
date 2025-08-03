# TreeNodeクラスの定義
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# この問題は、二分木の前順（preorder）走査を行う問題です。前順走査では、根ノード → 左の子ノード → 右の子ノードの順に各ノードを訪問し、その順序でノードの値を出力します。

# 問題の要件
# 与えられた二分木に対して、前順走査を行い、各ノードの値をリストとして返すことを求めています。

# 前順走査（Preorder Traversal）とは？
# 前順走査は、「根 → 左 → 右」の順序でノードを訪問する方法です。二分木の前順走査の手順は次のようになります：

# 根ノードを訪問する
# 左の子ノードに移動して訪問する
# 右の子ノードに移動して訪問する
# この問題は、二分木の前順（preorder）走査を行う問題です。
# 前順走査では、根ノード → 左の子ノード → 右の子ノードの順に各ノードを訪問し、
# その順序でノードの値を出力します。

# Solutionクラスの定義
class Solution:
    # preorderTraversalメソッドの定義
    # 引数: root - 二分木のルートノード
    # 戻り値: 前順走査で訪問したノードの値を格納したリスト
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # headは現在のノードを指すポインタ
        head = root
        # 右側の子ノードを記録するスタック
        stack = []
        # 結果を格納するリスト
        res = []

        # headがNoneでなく、またはスタックに要素がある限りループ
        while head or stack:
            if head:
                # 根ノードの値を結果リストに追加（前順走査の「根」のステップ）
                res.append(head.val)
                # 右の子ノードが存在する場合、後で処理するためスタックに追加
                if head.right:
                    stack.append(head.right)
                # 左の子ノードに移動（前順走査の「左」のステップ）
                head = head.left
            else:
                # 左のノードがない場合、スタックから右の子ノードを取り出し処理を続行
                head = stack.pop()

        # 前順走査で訪問したノードの値のリストを返す
        return res   


# 呼び出し箇所
if __name__ == "__main__":
    # 木構造の構築
    root = TreeNode(1)
    # root.left = TreeNode(4)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(11)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(1)

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # hasPathSumメソッドの呼び出し
    print(sol.preorderTraversal(root))