from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 配列の末尾に 0 を追加します。
        # これは、最上部に到達するための "無料のゴール地点" を表します。
        cost.append(0)  # 例: [10, 15, 20, 0]

        # コスト配列を後ろから更新して、最小コストを計算します。
        # 範囲は len(cost) - 4 から 0 まで。つまり最後から 3 番目の要素から開始。
        for i in range(len(cost) - 4, -1, -1):
            # 現在のステップ i のコストに次の 1 ステップまたは 2 ステップの最小コストを追加。
            cost[i] += min(cost[i+1], cost[i+2])
            # 例: ステップ 1 のコストが次のステップ 2, 3 の最小コストを加えて更新される。

        # 最初の 2 つのステップのコストの最小値を返します。
        # なぜなら、どちらからスタートしても良いので、より安い方を選択します。
        return min(cost[0], cost[1])

# コスト配列の例
cost = [10, 15, 20]

# Solution クラスのインスタンスを作成
solution = Solution()

# メソッドを呼び出して結果を取得
result = solution.minCostClimbingStairs(cost)

# 結果を出力
print(f"最小コスト: {result}")
