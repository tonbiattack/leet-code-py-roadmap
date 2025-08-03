# typingモジュールからList型をインポート
from typing import List

# 強力なペア (Strong Pair) の条件　問題文に記載してあった
# ペア (x, y) が「強力なペア」と見なされるには以下の条件を満たす必要があります：

# ∣
# 𝑥
# −
# 𝑦
# ∣
# ≤
# min
# ⁡
# (
# 𝑥
# ,
# 𝑦
# )
# ∣x−y∣≤min(x,y)


class Solution:
    # maximumStrongPairXor関数は、リストの強力なペアの中で最大のXOR値を求めるための関数です。
    # 引数には整数のリストnumsが渡されます。
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # 結果を保持する変数ansを初期化します。
        ans = 0

        # numsリストの各要素xについてループを開始します。
        for x in nums:
            # numsリストの各要素yについて再度ループを開始します。
            for y in nums:
                # abs(x - y) <= min(x, y) の条件で、(x, y)のペアが「強力なペア」であるかを確認します。
                # abs(x - y)はxとyの差の絶対値を計算し、min(x, y)はxとyのうち小さい方の値です。
                if abs(x - y) <= min(x, y):
                    # 「強力なペア」であれば、XOR演算 (x ^ y) の結果と現在のansを比較し、
                    # もし (x ^ y) が大きければansを更新します。
                    ans = max(ans, x ^ y)

        # 最大のXOR値を返します。
        return ans


# 呼び出し部分
# Solutionクラスのインスタンスを作成
solution = Solution()

# テスト用のリストを定義
nums = [5, 6, 7, 8]

# maximumStrongPairXor関数を呼び出し、結果を出力
# 関数呼び出し時にリストnumsを引数として渡します。
print(solution.maximumStrongPairXor(nums))  # この結果はリスト内の強力なペアの最大XOR値を出力します。
