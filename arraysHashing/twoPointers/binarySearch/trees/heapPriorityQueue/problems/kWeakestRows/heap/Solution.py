import heapq  # Python 標準ライブラリから優先度付きキュー（ヒープ）を使用
from typing import List  # 型ヒントを記述するためのモジュール

# ソリューションクラス
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        行列 mat の中から軍事力が最も弱い k 個の行を見つけ、そのインデックスを返す。
        
        mat: 2次元リスト（0と1で構成された行列）
        k: 最弱な行を何個返すか
        """
        heap = []  # 最大ヒープを格納するリスト

        # 各行の軍事力を計算し、ヒープに格納する
        for i, row in enumerate(mat):  # enumerateを使って行のインデックスと内容を取得
            strength = sum(row)  # 行内の 1 の合計値を計算
            # 最大ヒープに (-strength, -i) を挿入する
            heapq.heappush(heap, (-strength, -i))  # Pythonのヒープはデフォルトで最小ヒープのため符号反転
            if len(heap) > k:  # ヒープのサイズが k を超えた場合、最大値を削除
                heapq.heappop(heap)
        
        # ヒープ内のインデックスを取り出し、結果を昇順に並べて返す
        return [-i for _, i in sorted(heap, reverse=True)]  # sortedで整列し、インデックスを元に戻す

# Solution クラスのインスタンスを作成
solution = Solution()

# テストケースの行列と k の値
matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
k = 3

# 関数を呼び出し
result = solution.kWeakestRows(matrix, k)

# 結果を表示
print(result)  # 期待される出力: [2, 0, 3]
