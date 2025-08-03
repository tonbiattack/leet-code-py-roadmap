from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 1]
    print(f"hasDuplicate({nums}) => {solution.hasDuplicate(nums)}")  # Trueが出力される

