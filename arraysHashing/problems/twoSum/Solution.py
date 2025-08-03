from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(f"twoSum({nums}, {target}) => {solution.twoSum(nums, target)}")  # [0, 1]が出力される
# --- 呼び出し例 ---
# ここでは、nums = [2, 7, 11, 15] と target = 9 を使用して、2つの数のインデックスを取得します。
# 出力は [0, 1] で、nums[0] + nums[1] = 2 + 7 = 9 となります。
