# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 既存の解法コード (Balanced Binary Tree)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # 左のサブツリーの高さを取得
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # 左がバランスしていない

            # 右のサブツリーの高さを取得
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # 右がバランスしていない

            # 左右の高さ差が1を超えたらバランスしていない
            if abs(left_height - right_height) > 1:
                return -1

            # バランスしているので、現在の高さを返す
            return max(left_height, right_height) + 1

        # 最初に木の根からチェックする
        return check_height(root) != -1

# ヘルパー関数：配列から二分木を構築する関数


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    # テストケース1: root = [3,9,20,null,null,15,7]
    # root1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    solution = Solution()
    # result1 = solution.isBalanced(root1)
    # print(f"Test case 1: {result1}")  # Expected: True

    # テストケース2: root = [1,2,2,3,3,null,null,4,4]
    root2 = build_tree_from_list([1, 2, 2, 3, 3, None, None, 4, 4])
    result2 = solution.isBalanced(root2)
    print(f"Test case 2: {result2}")  # Expected: False

    # テストケース3: root = []
    root3 = build_tree_from_list([])
    result3 = solution.isBalanced(root3)
    print(f"Test case 3: {result3}")  # Expected: True
