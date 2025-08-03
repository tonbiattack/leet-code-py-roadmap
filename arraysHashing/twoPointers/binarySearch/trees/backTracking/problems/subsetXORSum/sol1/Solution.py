from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)  # 配列 nums の要素数を取得します
        total_sum = 0  # XOR の総和を格納する変数を初期化します
        # 0 から 2^n - 1 までの整数を使って、すべての部分集合を表現します
        for i in range(1 << n):
            subset_xor = 0  # 現在の部分集合の XOR 値を初期化します
            for j in range(n):
                # i の j ビット目が 1 かどうかをチェックします
                if i & (1 << j):
                    subset_xor ^= nums[j]  # ビットが 1 なら、subset_xor に nums[j] を XOR します
            total_sum += subset_xor  # 現在の部分集合の XOR 値を総和に加えます
        return total_sum  # すべての部分集合の XOR の総和を返します

# 呼び出し部分の作成
if __name__ == "__main__":
    solution = Solution()  # Solution クラスのインスタンスを作成します
    nums = [5, 1, 6]  # サンプルの入力リストを定義します
    result = solution.subsetXORSum(nums)  # メソッドを呼び出して結果を取得します
    print(f"すべての部分集合の XOR の総和は {result} です")  # 結果を表示します
