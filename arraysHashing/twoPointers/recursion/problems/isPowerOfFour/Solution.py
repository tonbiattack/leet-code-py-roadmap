class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # nが0以下の場合はべき乗にはなり得ない
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 4 == 0:
            return self.isPowerOfFour(n // 4)
        # nが3で割り切れない場合はFalseを返す
        return False