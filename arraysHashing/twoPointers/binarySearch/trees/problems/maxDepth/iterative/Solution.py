# TreeNodeクラスの定義
class TreeNode:
    """
    二分探索木のノードを表すクラス。

    Attributes:
        val (int): ノードの値
        left (TreeNode): 左の子ノード（存在しない場合はNone）
        right (TreeNode): 右の子ノード（存在しない場合はNone）
    """
    def __init__(self, x):
        """
        TreeNodeの初期化。

        Args:
            x (int): ノードに格納する値
        """
        self.val = x  # ノードの値
        self.left = None  # 左の子ノードへの参照
        self.right = None  # 右の子ノードへの参照


# Solutionクラスの定義
class Solution:
    """
    二分探索木の最大深さを計算するためのクラス。
    """
    def maxDepth(self, root: TreeNode) -> int:
        """
        与えられた二分探索木の最大の深さを計算します。

        深さ優先探索（DFS）をスタックを使用して行い、反復的にノードを探索して最大の深さを求めます。
        スタックに各ノードとその深さのペアを保持し、木の全体を探索しながら深さを更新します。

        Args:
            root (TreeNode): 二分探索木のルートノード
        
        Returns:
            int: 二分探索木の最大深さ。木が空の場合は0を返します。
        """
        depth = 0  # 現時点での最大深さを保持
        stack = [(root, 1)]  # ルートノードとその深さ1をスタックに入れる

        # スタックが空になるまで木を探索
        while stack:
            root, length = stack.pop()  # スタックからノードとその深さを取り出す
            if not root:  # ノードがNoneならばツリーは空
                return 0  # ツリーが空の場合、深さは0
            
            # 現在のノードの深さがこれまでの最大深さよりも大きければ更新
            if length > depth:
                depth = length

            # 右の子ノードが存在するならば、スタックにそのノードと深さ+1を追加
            if root.right:
                stack.append((root.right, length + 1))

            # 左の子ノードが存在するならば、スタックにそのノードと深さ+1を追加
            if root.left:
                stack.append((root.left, length + 1))

        return depth  # 木の最大深さを返す


# 呼び出し部分
if __name__ == "__main__":
    """
    手動で構築した二分探索木を用いて、最大の深さを計算します。

    ツリー構造:
        3
       / \
      9  20
        /  \
       15   7

    結果:
        このツリーの最大深さは3です。
    """
    root = TreeNode(3)  # ルートノード
    root.left = TreeNode(9)  # 左の子ノード
    root.right = TreeNode(20)  # 右の子ノード
    root.right.left = TreeNode(15)  # 右の子ノードの左
    root.right.right = TreeNode(7)  # 右の子ノードの右

    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # 最大深さを計算
    result = solution.maxDepth(root)

    # 結果を出力
    print("Maximum depth of the binary tree:", result)
