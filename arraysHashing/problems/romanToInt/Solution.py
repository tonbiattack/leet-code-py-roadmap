# Solutionクラスの定義
class Solution:
    def romanToInt(self, s: str) -> int:
        # ローマ数字とその対応する整数値を保持する辞書
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0  # 結果の初期値を0に設定
        
        # 文字列sを一文字ずつ処理
        for i in range(len(s)):
            # 特定の条件下で減算が必要かどうかをチェック
            # iが最後の文字でなく、かつ現在のローマ数字が次のローマ数字よりも小さい場合
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]  # 減算
            else:
                ans += m[s[i]]  # 加算
        
        return ans

# 呼び出し箇所
if __name__ == "__main__":
    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # ローマ数字を整数に変換する例
    # roman_str = "MCMXCIV"  # 例: 1994に相当するローマ数字
    roman_str = "IV"
    result = sol.romanToInt(roman_str)

    # 結果の出力
    print(f"The integer value of the Roman numeral {roman_str} is: {result}")
