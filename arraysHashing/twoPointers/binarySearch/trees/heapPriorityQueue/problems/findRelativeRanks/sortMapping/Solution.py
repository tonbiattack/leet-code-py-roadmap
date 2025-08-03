# 必要な型注釈をインポートします
from typing import List

# Solution クラスの定義
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        スコアリストに対して、それぞれの順位を計算し、特定の順位にメダル名を割り当てて返します。

        Args:
            score (List[int]): スコアのリスト。

        Returns:
            List[str]: 順位またはメダル名を含むリスト。
        """
        # スコアリストを降順にソートします
        # reverse=True により高いスコアが先に来るようにします
        sorted_score = sorted(score, reverse=True)
        
        # 特定の順位に割り当てるメダル名を定義します
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        # スコアをキーにして順位またはメダル名を値に持つ辞書を作成します
        # enumerate を使用して順位 (i) とスコア (score) をペアで取得します
        # 上位3位はメダル名、それ以外は順位そのものを文字列で割り当てます
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(sorted_score)}
        
        # 元のスコアリストに基づき、対応する順位やメダル名を取得して返します
        return [rank_mapping[s] for s in score]

# Solution クラスのインスタンスを作成
sol = Solution()

# テストケースを定義し、findRelativeRanks メソッドを呼び出します
# {5, 4, 3, 2, 1} は集合型で正しいリスト型ではないため修正
test_case = [5, 4, 3, 2, 1]

# 呼び出し結果を出力します
result = sol.findRelativeRanks(test_case)
print(result)  # 結果を表示
