import copy
from typing import Optional

class ListNode:
    """
    リンクリストのノードを表すクラス。
    
    Attributes:
        val (int): ノードの値。
        next (Optional[ListNode]): 次のノードを指すポインタ。
    """
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        tmp = copy.copy(stack)
        stack.reverse()
        return tmp == stack

# ノードを作成する関数（便宜的に作成）
def create_linked_list(values):
    """
    値のリストからリンクリストを生成する。

    Args:
        values (list): リンクリストに挿入する値のリスト。

    Returns:
        ListNode: 生成されたリンクリストの先頭ノード。
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# リンクリストを出力する関数
def print_linked_list(node):
    """
    リンクリストを出力する（デバッグ用）。

    Args:
        node (ListNode): リンクリストの先頭ノード。
    """
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# リンクリストを作成
list1 = create_linked_list([1, 2])
# Solutionクラスのインスタンスを作成し、hasCycleメソッドを呼び出す
solution = Solution()
print(solution.isPalindrome(list1))

