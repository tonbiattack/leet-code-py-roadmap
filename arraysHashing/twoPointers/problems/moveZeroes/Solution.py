from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        リスト nums 内のゼロを全て末尾に移動し、その他の要素の順序を維持します。
        インプレースでリストを変更し、何も返しません。
        """
        # nums リストを逆方向（右から左）にループします
        # len(nums)+1 を使用することで1からリストの長さまでの範囲でループします
        for i in range(1, len(nums) + 1):
            # 現在の要素が 0 の場合
            if nums[-i] == 0:
                # 現在の 0 をリストから削除します（インデックス -i で右端から指定）
                nums.pop(-i)
                # 0 をリストの末尾に追加します
                nums.append(0)
        # この方法により、元のリストの順序は保持されつつ、ゼロが末尾に移動します


# Solutionクラスのインスタンス化
sol = Solution()

# テストケース
nums1 = [0, 1, 0, 3, 12]
nums2 = [0, 0, 1]
nums3 = [1, 0, 0, 2, 3, 0, 4]

# 各テストケースで関数を呼び出し
sol.moveZeroes(nums1)
print(nums1)  # 出力例: [1, 3, 12, 0, 0]

sol.moveZeroes(nums2)
print(nums2)  # 出力例: [1, 0, 0]

sol.moveZeroes(nums3)
print(nums3)  # 出力例: [1, 2, 3, 4, 0, 0, 0]
