class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 長さが異なる場合、アナグラムではないため即座にFalseを返す
        if len(s) != len(t):
            return False

        # 各文字の出現回数を記録する辞書を初期化
        countS, countT = {}, {}

        # 文字列sとtの文字をそれぞれカウントする
        for i in range(len(s)):
            # s内の文字の出現回数をcountSに記録
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # t内の文字の出現回数をcountTに記録
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # 2つの辞書を比較し、同じであればTrue（アナグラム）、違えばFalseを返す
        return countS == countT

# 呼び出し部分
if __name__ == "__main__":
    # インスタンスを作成
    solution = Solution()

    # テストケース
    s1, t1 = "racecar", "carrace"
    s2, t2 = "jar", "jam"

    # メソッドの呼び出しと出力
    print(solution.isAnagram(s1, t1))  # 期待出力: True
    print(solution.isAnagram(s2, t2))  # 期待出力: False