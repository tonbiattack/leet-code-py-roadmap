class Solution:
    def reverseVowels(self, s: str) -> str:
        # 文字列をリストに変換。文字列はイミュータブル（変更不可能）なため、
        # リストにすることでインプレースでの文字操作が可能になる。
        s = list(s)
        
        # 文字列の長さを取得
        n = len(s)
        
        # 左右から探索するためのポインタを初期化
        left = 0
        right = n - 1
        
        # 母音の集合を定義。ここで大文字と小文字の母音をすべて含める。
        vowels = set('AEIOUaeiou')
        
        # 左右のポインタが交差するまでループを続ける
        while left < right:
            # 左側のポインタが母音でない場合、右方向へ進める
            while left < right and s[left] not in vowels:
                left += 1
            
            # 右側のポインタが母音でない場合、左方向へ進める
            while left < right and s[right] not in vowels:
                right -= 1
            
            # 左右のポインタが共に母音に当たっている場合、入れ替える
            s[left], s[right] = s[right], s[left]
            
            # 左右ポインタを更新して次の位置へ
            left += 1
            right -= 1
        
        # 文字列に戻して返す
        s = ''.join(s)
        return s

# Solutionクラスをインスタンス化
sol = Solution()

# テストケースを設定
s1 = "IceCreAm"
s2 = "hello"
s3 = "leetcode"
s4 = "aA"

# 各テストケースで関数を呼び出し
print(sol.reverseVowels(s1))  # 出力例: "AcICreEm"
print(sol.reverseVowels(s2))  # 出力例: "holle"
print(sol.reverseVowels(s3))  # 出力例: "leotcede"
print(sol.reverseVowels(s4))  # 出力例: "Aa"
