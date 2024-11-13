# typing モジュールから Optional をインポートしています。
# Optional は型ヒントとして使用され、値が None になる可能性がある場合に使用します。
from typing import Optional

# ListNode クラスの定義
# リンクリストの各ノードを表現するためのクラスです。
class ListNode:
    # 初期化メソッド __init__ を定義します。
    # ノードの値 val と次のノードへの参照 next を設定します。
    def __init__(self, val=0, next=None):
        self.val = val  # ノードの値（整数）
        self.next = next  # 次のノードへの参照。None であれば末端のノード

# Solution クラスの定義
# ここに問題の解決方法を実装します。
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

# 呼び出し部分
# このメソッドがどのように動作するかをテストするためにリンクリストを作成します。

# ノードを作成する関数（便宜的に作成）
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

# ソート済みのリンクリストを2つ作成します。
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Solution クラスのインスタンスを作成します。
solution = Solution()

# mergeTwoLists メソッドを呼び出して、2つのリストをマージします。
merged_list = solution.mergeTwoLists(list1, list2)

# マージされたリンクリストを出力します。
print("Merged Linked List:")
print_linked_list(merged_list)
