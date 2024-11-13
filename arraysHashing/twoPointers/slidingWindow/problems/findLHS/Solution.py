# collectionsモジュールとList型のサポートをインポート
import collections
from typing import List

# Solutionクラスの定義
class Solution:
    # findLHSメソッドを定義、整数のリストを引数として受け取り、最長調和部分列の長さを返す
    def findLHS(self, nums: List[int]) -> int:
        # collections.Counterを使用してnums内の各要素の出現回数をカウント
        count = collections.Counter(nums)
        # 答えを保持する変数ansを0で初期化
        ans = 0
        
        # countの各キーに対してループを実行
        for x in count:
            # x + 1がcount内に存在するかを確認
            # 存在する場合、xとx + 1の出現回数の合計が調和部分列になる
            if x + 1 in count:
                # 現在のansと新たに計算した部分列の長さを比較し、大きい方を選択
                ans = max(ans, count[x] + count[x + 1])
        
        # 最長調和部分列の長さを返す
        return ans

# Solutionクラスのインスタンスを作成し、テストケースでメソッドを呼び出して出力
sol = Solution()
print(sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
