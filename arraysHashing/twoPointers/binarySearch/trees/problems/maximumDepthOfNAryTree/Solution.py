# TreeNode クラスの定義
# Nodeクラスは、N分木の各ノードを表します。
# 各ノードには値（val）と、子ノード（children）があります。
from typing import List, Optional


class Node:
    # コンストラクタ __init__ は、ノードの値 val とその子ノードのリスト children を初期化します。
    # children はデフォルトで None で、指定がない場合、空のリストとして扱います。
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # maxDepth メソッドは、与えられた N 分木の最大深度を求めるためのものです。
    # root が与えられた N 分木のルートノードで、返り値として木の最大深度を整数で返します。
    def maxDepth(self, root: 'Node') -> int:
        # 基本ケース: root が None の場合、つまり木が空の場合、深さは 0 とする
        if not root:
            return 0

        # 深さの初期値を 1 と設定（ルートノード自体の深さを表す）
        depth = 1

        # 子ノードが存在する場合、再帰的に各子ノードの最大深度を取得
        # すべての子ノードの最大深度に 1 を加えることで、現在のノードからの深さを計算する
        if root.children:
            depth += max(self.maxDepth(child) for child in root.children)

        # 最終的な深さを返す
        return depth

# 以下は呼び出し箇所です。

# 例: 木構造の作成
#        1
#      / | \
#     3  2  4
#    / \
#   5   6

# ルートノードを作成
root = Node(1)

# 子ノードを追加
child1 = Node(3, [Node(5), Node(6)])  # 3の子として5と6を追加
child2 = Node(2)
child3 = Node(4)

# ルートの子に上記のノードを追加
root.children = [child1, child2, child3]

# Solution クラスのインスタンスを作成し、maxDepth メソッドを呼び出して最大深度を求める
solution = Solution()
print("木の最大深度:", solution.maxDepth(root))  # 期待される出力は 3
