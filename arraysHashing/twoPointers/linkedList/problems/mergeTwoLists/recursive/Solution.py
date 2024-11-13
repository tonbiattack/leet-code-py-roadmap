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
    # mergeTwoLists メソッドの定義
    # 2つのソート済みリンクリスト list1 と list2 をマージし、1つのソート済みリンクリストを返します。
    # 引数 list1 と list2 はどちらも ListNode 型のオブジェクトであり、Optional[ListNode] 型ヒントが付与されています。
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ベースケース：どちらかのリストが空である場合、そのままもう一方のリストを返します。
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # 再帰的にマージする
        # まず、list1.val と list2.val を比較します。
        if list1.val <= list2.val:
            # list1 の値が list2 の値以下の場合、list1 が先に来るべきなので、
            # list1 の次の要素として再帰的に mergeTwoLists(list1.next, list2) を設定します。
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # 逆に、list2 の値が list1 の値より小さい場合は、list2 が先に来るべきです。
            # そのため、list2 の次の要素として再帰的に mergeTwoLists(list1, list2.next) を設定します。
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

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
