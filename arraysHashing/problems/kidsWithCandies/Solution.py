from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        各子供が持っているキャンディーの数に追加のキャンディーを加えたとき、
        その子供が最大のキャンディー数を持つかどうかを判定する。

        Args:
            candies (List[int]): 各子供が持っているキャンディーのリスト
            extraCandies (int): 各子供に追加できるキャンディーの数

        Returns:
            List[bool]: 各子供が最大のキャンディー数を持つかどうかを判定した結果のリスト
        """
        num = max(candies)  # 現時点での最大のキャンディー数を取得
        for i in range(len(candies)):
            if candies[i] + extraCandies >= num:
                candies[i] = True  # 追加した結果、最大数以上ならTrue
            else:
                candies[i] = False  # それ以外はFalse
        return candies  # 判定結果のリストを返す

# 呼び出し部分
if __name__ == "__main__":
    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # サンプル入力
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    # メソッドを呼び出し、結果を取得
    result = solution.kidsWithCandies(candies, extraCandies)

    # 結果を出力
    print("Result of kidsWithCandies:", result)
