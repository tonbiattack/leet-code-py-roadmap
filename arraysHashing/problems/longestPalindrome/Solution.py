class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 奇数回出現する文字の数をカウントする変数
        odd_count = 0
        # 各文字とその出現回数を記録する辞書
        d = {}

        # 入力文字列の各文字をループする
        for ch in s:
            # 文字が既に辞書にある場合はカウントを増やす
            if ch in d:
                d[ch] += 1
            else:
                # 文字が辞書にない場合は、新しいエントリを作成
                d[ch] = 1

            # 出現回数が奇数の場合、odd_countを増やす
            if d[ch] % 2 == 1:
                odd_count += 1
            else:
                # 出現回数が偶数の場合、odd_countを減らす
                odd_count -= 1

        # 奇数回出現する文字が2つ以上ある場合
        if odd_count > 1:
            # 回文の長さは、全体の長さから余分な奇数回の文字を調整したもの
            return len(s) - odd_count + 1

        # 奇数回出現する文字が1つ以下の場合、全体が回文になる
        return len(s)


if __name__ == "__main__":
    # 入力の例
    input_string = "abccccdd"

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # longestPalindrome メソッドを呼び出して結果を取得
    result = solution.longestPalindrome(input_string)

    # 結果を出力
    print(f"入力文字列: {input_string}")
    print(f"最長回文の長さ: {result}")
