import heapq  # Python 標準ライブラリから優先度付きキュー（ヒープ）を使用
from typing import List  # 型ヒントを記述するためのモジュール

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = [(sum(row), i) for i, row in enumerate(mat)]
        row_strength.sort(key=lambda x: (x[0], x[1]))
        return [row[1] for row in row_strength[:k]]

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
