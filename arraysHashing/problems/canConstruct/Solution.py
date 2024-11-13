# collections モジュールから Counter クラスをインポート
# Counter は要素の出現回数をカウントする辞書型のデータ構造
from collections import Counter

# Solution クラスの定義
class Solution(object):
    # canConstruct メソッド: ransomNote が magazine の文字だけで構成できるかを確認
    def canConstruct(self, ransomNote, magazine):
        # ransomNote と magazine の文字の出現回数をカウントして Counter オブジェクトを作成
        st1, st2 = Counter(ransomNote), Counter(magazine)

        # st1（ransomNote の文字カウント）と st2（magazine の文字カウント）を比較
        # st1 & st2 は、各文字について両者に共通する最小の出現回数を含む Counter オブジェクト
        # もし st1 & st2 が st1 と同じなら、ransomNote の文字すべてが magazine で提供されている
        if st1 & st2 == st1:
            return True  # 構成可能な場合、True を返す
        return False  # 構成不可能な場合、False を返す

# Solution インスタンスの生成
sol = Solution()

# canConstruct メソッドのテスト
# "aa" を "aab" から構成できるかをチェック
# print(sol.canConstruct("aa", "aab"))  # True を期待

# "aa" を "ab" から構成できるかをチェック
print(sol.canConstruct("aa", "ab"))  # False を期待
