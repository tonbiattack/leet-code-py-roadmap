from typing import List

# 問題解説:
# 配列の中で出現頻度が高い上位k個の要素を求める問題です。
# 例えば [1,1,1,2,2,3] で k=2 の場合、1と2が最も多く出現するので [1,2] を返します。
#
# 解法:
# collections.Counter を使って各要素の出現回数を数えます。
# Counter.most_common(k) で頻度の高い順にk個の要素を取得できます。
# その結果から要素のみをリストで返します。

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)   # 各要素の頻度をカウント
        return [num for num, freq in count.most_common(k)] # 上位k個の頻度の高い要素を取得

# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"topKFrequent({nums}, {k}) => {solution.topKFrequent(nums, k)}")