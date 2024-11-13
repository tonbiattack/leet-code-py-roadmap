from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # ベースケース: リストが空の場合
        if head is None:
            return None

        # 再帰的に次のノードを処理
        head.next = self.removeElements(head.next, val)

        # 現在のノードが削除対象かどうかをチェック
        # 削除対象である場合はhead.nextに現在のhead.nextを追加して今回の要素をスキップできるようにする
        # 削除対象でない場合はhead.nextに今回のheadを接合して順番を飛ばさないようにする
        return head.next if head.val == val else head

# リンクリストを作成する関数
def create_linked_list(values):
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
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# テストケース
list1 = create_linked_list([1, 2, 6, 3, 4, 5, 6])
solution = Solution()
result = solution.removeElements(list1, 6)
print_linked_list(result)
