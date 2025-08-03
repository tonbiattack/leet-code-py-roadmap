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
    def postorder(self, root: 'Node') -> List[int]:
        # 結果を保存するリストを初期化
        result = []

        # 深さ優先探索のヘルパー関数
        def dfs(node: 'Node'):
            # 基本ケース: ノードが None の場合は戻る
            if not node:
                return
            
            # 子ノードをすべて訪問する
            for child in node.children:
                dfs(child)

            # 子ノードをすべて訪問した後に現在のノードを追加（ポストオーダーのため）
            result.append(node.val)

        # ルートノードから深さ優先探索を開始
        dfs(root)
        return result

# 以下は呼び出し箇所の例です。

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

# Solution クラスのインスタンスを作成し、postorder メソッドを呼び出してポストオーダーを求める
solution = Solution()
print("木のポストオーダー:", solution.postorder(root))  # 期待される出力は [5, 6, 3, 2, 4, 1]
