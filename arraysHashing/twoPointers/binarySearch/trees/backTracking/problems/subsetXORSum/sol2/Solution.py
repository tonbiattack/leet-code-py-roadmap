from typing import List

from typing import List

# 1 << (n-1) を使う理由: 部分集合の総数は 
# 2
# 𝑛
# 2 
# n
#   であり、ある要素が含まれる部分集合の数は 
# 2
# 𝑛
# −
# 1
# 2 
# n−1
#   個であるためです。
from typing import List  # 型アノテーションのために List をインポート

# Solution クラスを定義
class Solution:
    # subsetXORSum メソッドを定義: 入力は整数のリスト、出力は整数
    def subsetXORSum(self, nums: List[int]) -> int:
        # リストの長さ n を取得
        # n は nums の要素数を表す（部分集合の数に影響を与える）
        n = len(nums)  
        
        # all_or を 0 に初期化（すべての要素のビット和を格納するための変数）
        all_or = 0  
        
        # リストのすべての要素についてループ
        for i in range(n):
            # all_or に現在の要素 nums[i] をビットOR演算で追加
            # |= はビット単位の OR を行う複合代入演算子
            all_or |= nums[i]
            # 例: nums = [1, 3, 5] の場合
            # 1. 初回: all_or = 0 | 1 = 1
            # 2. 次回: all_or = 1 | 3 = 3
            # 3. 最後: all_or = 3 | 5 = 7
        
        # 部分集合における要素の出現回数を考慮して XOR の総和を計算
        # 各要素が含まれる部分集合の数は 2^(n-1) 個である
        # 全体の部分集合の XOR の総和は all_or に 2^(n-1) を掛けた値
        return all_or * (1 << (n - 1))
        # 1 << (n-1) はビットシフト演算で 2^(n-1) を計算
        # 例: n = 3 の場合、1 << (3-1) = 1 << 2 = 4



# 呼び出し部分の作成
if __name__ == "__main__":
    solution = Solution()  # Solution クラスのインスタンスを作成します
    nums = [1, 3, 5]  # サンプルの入力リストを定義します
    result = solution.subsetXORSum(nums)  # メソッドを呼び出して結果を取得します
    print(f"すべての部分集合の XOR の総和は {result} です")  # 結果を表示します
