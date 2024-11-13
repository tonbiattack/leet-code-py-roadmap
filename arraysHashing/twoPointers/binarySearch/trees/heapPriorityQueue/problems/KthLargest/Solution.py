import heapq  # heapqライブラリのインポート。最小ヒープ操作が可能です。
from typing import List  # 型ヒントとしてListを使用します。

# このコードは、ストリームで「k番目に大きい要素」を効率的に管理するためのKthLargestクラスを実装しています。
# Pythonのheapqモジュールを使用しており、minHeapを使ってk番目に大きい値を維持するために最小ヒープを利用します。


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        コンストラクタメソッド
        k: k番目に大きい値を追跡するための整数。
        nums: 初期の整数のリスト。
        """
        # 最小ヒープとしてnumsを格納し、kをインスタンス変数として保存します。
        self.minHeap, self.k = nums, k
        # numsを最小ヒープに変換します。
#         Pythonにおけるヒープの実装
# Pythonには、ヒープを簡単に扱えるライブラリheapqが用意されています。このライブラリは最小ヒープとして動作し、以下のような関数が提供されています。

# heapq.heapify(list): リストを最小ヒープに変換します。
# heapq.heappush(heap, item): ヒープに新しい要素を追加し、ヒープ条件を満たすようにします。
# heapq.heappop(heap): ヒープから最小値を取り出し、ヒープ条件を満たすようにします。
# heapq.nsmallest(n, iterable): リストからn個の最小要素を返します。
        heapq.heapify(self.minHeap)  # O(n)の操作。全体をヒープ化して最小値が先頭に来るようにします。

        # ヒープのサイズがkを超えている間、最小の要素を取り除きます。
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)  # ヒープから最小値を削除します。

    def add(self, val: int) -> int:
        """
        valを追加し、現在のk番目に大きい要素を返します。
        """
        # 新しい要素をヒープに追加します。
        heapq.heappush(self.minHeap, val)  # O(log k)の操作。valを追加して、ヒープ構造を維持します。

        # ヒープサイズがkを超える場合、最小値を削除してk個の要素のみを維持します。
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # O(log k)の操作。k個以上の場合、最小値を取り除きます。

        # k番目に大きい値は、minHeapの先頭にある要素です。
        return self.minHeap[0]  # minHeap[0]は、k番目に大きい要素です。
