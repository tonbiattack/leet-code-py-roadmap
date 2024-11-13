class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # ベースケース：nが1ならば2のべき乗なのでTrueを返す
        if n == 1:
            return True
        # nが1未満または2で割り切れない場合は2のべき乗ではない
        if n <= 0 or n % 2 != 0:
            return False
        # 2で割り続けて再帰的に確認
        return self.isPowerOfTwo(n // 2)

solution = Solution()
print(solution.isPowerOfTwo(3))  # False
print(solution.isPowerOfTwo(4))  # True
