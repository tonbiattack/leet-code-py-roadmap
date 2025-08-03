from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 各値の出現回数を記録する辞書
        self.mode_count = defaultdict(int)

        # 深さ優先探索の定義
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            # ノードの値をカウント
            self.mode_count[node.val] += 1
            # 右の子ノードと左の子ノードを再帰的に探索
            dfs(node.right)
            dfs(node.left)

        # DFSの開始
        dfs(root)

        # 最大出現回数を取得
        max_count = max(self.mode_count.values(), default=0)

        # 出現回数が最大の値（最頻値）を全てリストに追加

# この記法は、リスト内包表記と呼ばれる Python の記法です。リスト内包表記は、リストを生成するための簡潔で読みやすい方法です。

# 解説
# python
# コードをコピーする
# modes = [key for key, count in self.mode_count.items() if count == max_count]
# 各部分の説明
# modes = [...]: この全体がリスト内包表記で、結果としてリスト modes に値が代入されます。
# [key for key, count in self.mode_count.items() if count == max_count]: リスト内包表記の構造で、条件に基づいたリストを生成しています。
# 各構成要素
# key for key, count in self.mode_count.items():

# self.mode_count.items() は、辞書 self.mode_count のキーと値のペアを取り出すためのメソッドです。この場合、key が辞書のキー、count がそのキーに対応する値（出現回数）になります。
# for key, count in self.mode_count.items() は、辞書の各キーとその出現回数を順に取り出し、ループ処理を行います。
# if count == max_count:

# if 条件はオプションで、ループ中に条件を満たす要素のみをリストに追加するためのフィルタリングとして使われます。
# ここでは、count == max_count という条件を満たす場合のみ、key がリストに追加されます。つまり、最頻値（最大出現回数）を持つキーだけがリストに追加されるようになっています。
# 結果
# このリスト内包表記により、self.mode_count の中で count == max_count の条件を満たすキーのみを含むリストが生成され、modes に代入されます。
# 具体的には、self.mode_count の中で最大の出現回数 max_count を持つキーがすべて modes に含まれます。
# 例
# 例えば、self.mode_count = {1: 2, 2: 3, 3: 3} で、max_count = 3 の場合、リスト内包表記の結果は次のようになります：

# python
# コードをコピーする
# modes = [key for key, count in {1: 2, 2: 3, 3: 3}.items() if count == 3]
# # 出力: [2, 3]
# このように、最大出現回数を持つキー 2 と 3 のみがリスト modes に格納されます。
        modes = [key for key, count in self.mode_count.items() if count ==
                 max_count]

        return modes


# 呼び出し箇所の例
if __name__ == "__main__":
    # 木構造の構築
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(1)
    root.right.left = TreeNode(2)
    # root.right.right = TreeNode(1)

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # findModeメソッドの呼び出し
    print(sol.findMode(root))  # 期待される出力は [2]
