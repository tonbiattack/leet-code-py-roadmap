# 必要な型注釈をインポートします
import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        与えられた選手のスコアリストに基づいて、順位を文字列形式で返す。
        """
        N = len(score)  # 選手の人数を取得

        # ヒープを使ってスコアの順位を管理する
        heap = []
        for index, s in enumerate(score):
            # スコアを負にしてヒープに格納 (降順で取り出すため)
            heapq.heappush(heap, (-s, index))  # (スコア, インデックス)

        # 各選手の順位を格納するリスト
        rank = [0] * N
        place = 1  # 現在の順位を管理する変数

        while heap:
            # ヒープからスコアが最も高い選手のインデックスを取得
            original_index = heapq.heappop(heap)[1]

            # 順位に応じてメダルや順位を割り当て
            if place == 1:
                rank[original_index] = "Gold Medal"  # 1位は金メダル
            elif place == 2:
                rank[original_index] = "Silver Medal"  # 2位は銀メダル
            elif place == 3:
                rank[original_index] = "Bronze Medal"  # 3位は銅メダル
            else:
                rank[original_index] = str(place)  # 4位以降は順位を文字列で記録

            # 次の順位に進む
            place += 1

        return rank


# Solution クラスのインスタンスを作成
sol = Solution()

# テストケースを定義し、findRelativeRanks メソッドを呼び出します
# {5, 4, 3, 2, 1} は集合型で正しいリスト型ではないため修正
test_case = [1, 2, 3, 4, 5]

# 呼び出し結果を出力します
result = sol.findRelativeRanks(test_case)
print(result)  # 結果を表示
