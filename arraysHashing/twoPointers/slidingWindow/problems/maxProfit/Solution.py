from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

# テスト関数
def test_max_profit():
    # テストケースを定義
    test_cases = [
        [7, 1, 5, 3, 6, 4],  # 1日目に買って5日目に売ると利益5
        [7, 6, 4, 3, 1],     # 株価が下がり続ける場合、利益は0
        [2, 4, 1],           # 2日目に買って4日目に売ると利益2
        [3, 3, 5, 0, 0, 3, 1, 4],  # 5日目に買って8日目に売ると利益4
    ]

    # Solution クラスのインスタンスを作成
    solution = Solution()
    
    # 各テストケースで maxProfit を呼び出し、結果を表示
    for prices in test_cases:
        print(f"Input prices: {prices}")
        result = solution.maxProfit(prices)
        print(f"Maximum Profit: {result}\n")

# main 関数
if __name__ == "__main__":
    test_max_profit()    