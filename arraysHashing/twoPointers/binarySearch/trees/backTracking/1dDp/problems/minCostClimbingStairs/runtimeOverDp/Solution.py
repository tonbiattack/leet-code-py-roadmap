from typing import List

# 以下に、minCostClimbingStairs の問題に対する解説およびコードのコメント付き実装を記述します。

# 問題概要
# 与えられた配列 cost は、階段を登るためのコストを示しています。

# 配列の各要素は特定のステップに到達するためのコストです。
# 最後の階段に到達するために支払う最小コストを求めます。
# 階段のどのステップからでもスタートできますが、階段を1ステップまたは2ステップずつしか登れません。
# 解法
# この問題は、**動的計画法（Dynamic Programming, DP）**を用いて解くことができます。
# 以下の手順で考えます：

# 再帰的な関数を定義し、サブプロブレムを解く。
# 各ステップに到達するための最小コストを再帰的に計算。
# 最後のステップを考慮し、結果を返します。


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        階段を登る最小コストを計算する関数。

        Args:
            cost (List[int]): 各ステップに到達するためのコストを格納した配列。

        Returns:
            int: 最小コスト。
        """
        # 内部で使用する再帰的な関数を定義。
        # dp(n): ステップ n に到達するための最小コストを返す。
        def dp(n):
            """
            ステップ n に到達するための最小コストを計算する再帰関数。

            Args:
                n (int): 現在のステップ番号。

            Returns:
                int: ステップ n に到達するための最小コスト。
            """
            # ベースケース: 最初の2ステップはコストそのまま。
            if n < 2:
                return cost[n]

            # 再帰関係式:
            # ステップ n に到達するには、(n-1) または (n-2) から来るしかない。
            # この時の最小コストを計算。
            return cost[n] + min(dp(n - 1), dp(n - 2))

        # 階段の長さを取得。
        length = len(cost)

        # 最後のステップに到達するためのコストを計算:
        # 長さ-1 (最後のステップ) または 長さ-2 (最後の1つ手前のステップ) の最小コストを考慮。
        return min(dp(length - 1), dp(length - 2))


if __name__ == "__main__":
    solution = Solution()

    # 入力例
    # ステップごとの計算
    # dp(0) = 10
    # dp(1) = 15
    # dp(2) = cost[2] + min(dp(1), dp(0)) = 20 + min(15, 10) = 30
    # 結果として、min(dp(1), dp(2)) = min(15, 30) = 15。
    cost = [10, 15, 20]

    # 関数を呼び出して結果を取得
    result = solution.minCostClimbingStairs(cost)

    # 結果を出力
    print(f"The minimum cost to climb the stairs is: {result}")
