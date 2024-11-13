class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # nが0以下の場合はべき乗にはなり得ない
        if n <= 0:
            return False
        # nが1の場合は3のべき乗（3^0）に当たるためTrueを返す
        if n == 1:
            return True
        # それ以外の場合、nが3で割り切れるなら再帰的に確認
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        # nが3で割り切れない場合はFalseを返す
        return False

# テスト
solution = Solution()
print(solution.isPowerOfThree(9))  # True
print(solution.isPowerOfThree(27)) # True
print(solution.isPowerOfThree(10)) # False
