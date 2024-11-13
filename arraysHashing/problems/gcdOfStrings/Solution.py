class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 2つの文字列 str1 と str2 を結合した結果が等しくない場合、共通の最大部分文字列は存在しない
        # 例えば、str1 + str2 と str2 + str1 が異なる場合、2つの文字列は共通するパターンを持っていないため "" を返す
        if str1 + str2 != str2 + str1:
            return ""

        # 両方の文字列が同じパターンで構成されている場合、2つの文字列の長さの最大公約数（gcd）に対応する部分文字列を返す
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]

# 呼び出し例
if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    sol = Solution()
    # 出力: ABC （str1 と str2 は共通の文字列パターン "ABC" を持っている）
    print(sol.gcdOfStrings(str1, str2))
