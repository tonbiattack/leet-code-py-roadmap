from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))
        
        return min(dfs(0), dfs(1))

# メイン関数が呼び出しの起点
if __name__ == "__main__":
    # Solution クラスのインスタンス化
    solution = Solution()
    
    # 段数を指定して関数を呼び出し
    # 例: n=3 の場合
    result = solution.climbStairs(3)
    
    # 結果を出力
    # この場合、結果は 3 が出力される (1+1+1, 1+2, 2+1)
    print(result)
