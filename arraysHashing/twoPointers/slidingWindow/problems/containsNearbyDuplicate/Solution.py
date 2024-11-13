from typing import List


class Solution:
    # このコードは、nums配列の中に距離 k 以下の範囲で重複している要素があるかどうかを判定する関数 containsNearbyDuplicate を定義しています。
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 辞書 hset を作成して、各要素の最後に出現したインデックスを保持
        hset = {}

        # nums 配列の各要素をインデックスと共に走査
        for idx in range(len(nums)):
            # 現在の要素 nums[idx] が hset に既に存在し、かつインデックスの差が k 以下なら True を返す
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True

            # 現在の要素 nums[idx] を辞書に登録または更新し、最新のインデックスを保存
            hset[nums[idx]] = idx

        # 配列のすべての要素を確認しても条件を満たさない場合、False を返す
        return False


# インスタンスを作成してテストケースを確認する
solution = Solution()

# テストケース1: 重複が存在し、距離が k 以内なので True
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True

# テストケース2: 重複が存在し、距離が k を超えるが、別の重複が k 以内に存在するので True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True

# テストケース3: 重複が存在しないので False
print(solution.containsNearbyDuplicate([1, 2, 3, 4], 1))  # False

# テストケース4: 重複が存在するが、距離が k を超えているため False
print(solution.containsNearbyDuplicate([1, 2, 3, 4, 1], 3))  # False
