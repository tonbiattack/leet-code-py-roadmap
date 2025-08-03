from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 1]
    print(f"hasDuplicate({nums}) => {solution.hasDuplicate(nums)}")  # Trueが出力される

