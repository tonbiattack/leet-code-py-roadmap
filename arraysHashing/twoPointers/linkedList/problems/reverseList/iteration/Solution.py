from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # ノードの値
        self.next = next  # 次のノードへの参照（Noneであれば末端のノード）

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
# 呼び出し部分の例
# リストを作成します。例えば、1 -> 2 -> 3 -> 4 -> 5 のリンクリストを構築します。
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# ソリューションインスタンスを作成し、reverseListメソッドを呼び出してリストを反転させます。
solution = Solution()
reversed_head = solution.reverseList(head)

# 結果を出力して確認します。反転後のリストは5 -> 4 -> 3 -> 2 -> 1 になります。
# 反転したリストを辿って結果を表示する関数
def printList(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# 反転後のリストを出力します
printList(reversed_head)