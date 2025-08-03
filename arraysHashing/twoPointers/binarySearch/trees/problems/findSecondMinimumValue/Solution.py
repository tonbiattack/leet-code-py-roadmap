# TreeNodeクラスの定義
from typing import Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        nums = []
        nodes = [root]
        while nodes:
            t = nodes.pop()
            nums.append(t.val)
            if t.left:
                nodes.append(t.left)
            if t.right:
                nodes.append(t.right)
        
        if len(set(nums)) == 1:
            return -1
        
        return sorted(set(nums))[1]

# 呼び出し箇所
if __name__ == "__main__":
    # 木構造の構築
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # findTargetメソッドの呼び出し
    print(sol.findTarget(root, 9))  # 期待される出力は True（5 + 4 = 9）
    print(sol.findTarget(root, 3))  # 期待される出力は False
