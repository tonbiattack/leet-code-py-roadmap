from typing import List

# 配列に重複が存在するか判定するクラス
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 配列の各要素を2重ループで比較
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 同じ値が見つかった場合Trueを返す
                if nums[i] == nums[j]:
                    return True
        # 重複がなければFalseを返す
        return False

# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 1]
    print(f"hasDuplicate({nums}) => {solution.hasDuplicate(nums)}")  # Trueが出力される

