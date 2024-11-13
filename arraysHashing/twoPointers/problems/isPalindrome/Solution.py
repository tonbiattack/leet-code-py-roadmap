class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ポインタを初期化: l は左端、r は右端
        l, r = 0, len(s) - 1

        # ポインタが交差するまでループ
        while l < r:
            # 左側のポインタが英数字になるまで右へ移動
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # 右側のポインタが英数字になるまで左へ移動
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # 大文字小文字を区別せずに比較
            if s[l].lower() != s[r].lower():
                return False  # 異なる文字があれば回文ではない

            # ポインタを次の位置へ移動
            l, r = l + 1, r - 1

        # すべてのチェックが通った場合は回文
        return True
    
    def alphaNum(self, c: str) -> bool:
        # 文字がアルファベットまたは数字かどうかを判定
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

# 呼び出し箇所の例
solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))  # 出力: True
print(solution.isPalindrome("tab a cat"))                    # 出力: False
