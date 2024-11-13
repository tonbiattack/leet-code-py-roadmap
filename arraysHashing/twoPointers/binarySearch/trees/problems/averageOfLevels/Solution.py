# 必要なモジュールのインポート
from collections import defaultdict
from typing import List, Optional

# TreeNode クラスの定義
class TreeNode:
    # TreeNodeクラスのコンストラクタ
    # val: ノードの値（デフォルト0）
    # left: 左の子ノード（デフォルトNone）
    # right: 右の子ノード（デフォルトNone）
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution クラスの定義
class Solution:
    # averageOfLevels メソッド：各レベルの平均値を求める
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # lvlcnt: 各レベルのノード数を保持する辞書
        lvlcnt = defaultdict(int)
        # lvlsum: 各レベルのノード値の合計を保持する辞書
        lvlsum = defaultdict(int)

        # 深さ優先探索 (DFS) メソッド
        # node: 現在のノード、level: 現在のレベル
        def dfs(node=root, level=0):
            # ベースケース：ノードがNoneなら処理終了
            if not node:
                return
            # 現在のレベルのノード数と値の合計を更新
            lvlcnt[level] += 1
            lvlsum[level] += node.val
            # 左の子ノードに対して再帰的にDFSを実行
            dfs(node.left, level+1)
            # 右の子ノードに対して再帰的にDFSを実行
            dfs(node.right, level+1)

        # DFSの開始呼び出し
        dfs()

        # 各レベルの平均を計算し、リストとして返す
        return [lvlsum[i] / lvlcnt[i] for i in range(len(lvlcnt))]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Solutionインスタンスを生成して、averageOfLevelsメソッドを呼び出し
solution = Solution()
print(solution.averageOfLevels(root))  # 各レベルの平均値が出力されるはずです
