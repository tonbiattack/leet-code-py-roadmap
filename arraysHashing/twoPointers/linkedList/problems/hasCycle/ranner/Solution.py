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

class Solution:
    """
    リンクリストに循環が存在するかを検出するクラス。

    メソッド:
        hasCycle(head: Optional[ListNode]) -> bool:
            与えられたリンクリストに循環が存在するかを判定する。
    """
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        リンクリストに循環が存在するかを判定する。
        
        Floyd's Cycle-Finding Algorithm（通称「2ポインタ法」）を使用。
        1つのポインタ（slow_pointer）は1ステップずつ進み、
        もう1つのポインタ（fast_pointer）は2ステップずつ進む。
        もしリストに循環が存在する場合、これら2つのポインタは必ず同じノードで合流する。
        
        Args:
            head (Optional[ListNode]): リンクリストの先頭ノード。

        Returns:
            bool: 循環が存在する場合はTrue、存在しない場合はFalse。
        """
        # 2つのポインタを初期化
        slow_pointer = head
        fast_pointer = head
        
        # fast_pointerが末端に到達するまでループ
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next           # slow_pointerは1ステップ進む
            fast_pointer = fast_pointer.next.next      # fast_pointerは2ステップ進む
            
            # ポインタが合流する場合、循環が存在することを示す
            if slow_pointer == fast_pointer:
                return True
        
        # fast_pointerが末端に到達した場合、循環は存在しない
        return False

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
list1 = create_linked_list([1, 2, 4])

# リンクリストに循環を作成（便宜上、最後のノードを最初のノードに接続）
list1.next.next.next = list1  # リンクリストに循環を作成する

# Solutionクラスのインスタンスを作成し、hasCycleメソッドを呼び出す
solution = Solution()
has_cycle = solution.hasCycle(list1)   # 循環の有無を確認

# 結果を表示
print("循環があります" if has_cycle else "循環がありません")
