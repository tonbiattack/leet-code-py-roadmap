# リンクリストのノードを定義するクラス
# valにはノードの値が、nextには次のノードの参照が入ります。
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # ノードの値
        self.next = next  # 次のノードへの参照（Noneであれば末端のノード）

# ソリューションのクラス
# reverseList メソッドでリンクリストを反転させます。
class Solution:
    # reverseListメソッド
    # head はリンクリストの先頭ノードを指すオブジェクトです。
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ベースケース：headがNone（リンクリストが空の場合）であれば、Noneを返して終了します。
        if not head:
            return None

        # 再帰で反転した新しい先頭ノードを保持する変数newHeadを用意します。
        newHead = head  # newHeadを初期化します。これを後で再帰の結果で更新します。

        # 再帰ケース：現在のノードが末端でなければ、再帰的にリストを反転させます。
        # head.next が Noneでなければ、再帰呼び出しでリストを逆にしていきます。
        if head.next:
            # 新しい先頭を得るために再帰的に呼び出します。
            newHead = self.reverseList(head.next)

            # 逆方向にポインタをつなぎ替えます。
            # 例えば、リストの2番目のノードが3番目のノードを指すようにします。
            # 再帰処理：リンクリストがまだ続く場合、再帰的に reverseList を呼び出して、次のノードから先を逆転させます。
            # head.next.next = head によって、現在のノードを次のノードの次（逆方向）に設定し、リンクリストのつなぎ方を逆にします。
            head.next.next = head

        # 元の方向のポインタをNoneに設定してループを防ぎます。
        head.next = None

        # 反転後のリストの新しい先頭ノードを返します。
        return newHead

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
