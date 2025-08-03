from itertools import combinations
from typing import List

# 解説
# この問題では、2つの文字列が与えられた場合に、1つ目の文字列が2つ目の文字列の**接頭辞（prefix）かつ接尾辞（suffix）**であるようなペアの数を数えます。

# ポイント:

# 接頭辞（prefix）： 文字列の先頭から部分的に一致する文字列。
# 接尾辞（suffix）： 文字列の末尾から部分的に一致する文字列。
# Pythonのitertools.combinationsを用いて、入力された文字列リストから全ての2つのペアを生成します。
class Solution:
    # メインメソッド: 文字列リストwordsを受け取り、条件を満たすペアの数を返します。
    def countPrefixSuffixPairs(self, words: List[str], ans=0) -> int:
        """
        words: 文字列のリスト
        ans: 条件を満たすペアのカウントを初期化 (デフォルトは0)

        Returns:
            条件を満たすペアの合計数
        """
        # itertools.combinationsを用いてwordsから2つの要素を選んだ全ペアを生成します。
        for pre_suf, word in combinations(words, 2):  # combinations(words, 2)はペアのイテラブルを返します。
            # wordがpre_sufをprefixとして持ち、かつsuffixとしても持つ場合、ansをインクリメントします。
            ans += word.startswith(pre_suf) and word.endswith(pre_suf)
            # word.startswith(pre_suf): wordがpre_sufで始まる場合True。
            # word.endswith(pre_suf): wordがpre_sufで終わる場合True。
            # 両方がTrueならand条件で1を足します。

        # 最終的なカウント結果を返します。
        return ans


# 呼び出し箇所の例
if __name__ == "__main__":
    # テスト用の文字列リスト
    words = ["a","aba","ababa","aa"]
    # Solutionクラスのインスタンスを作成
    solution = Solution()
    # countPrefixSuffixPairsメソッドを呼び出し、結果を出力
    result = solution.countPrefixSuffixPairs(words)
    print(f"条件を満たすペアの数: {result}")