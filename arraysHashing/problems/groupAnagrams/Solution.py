from typing import List

# 問題解説:
# 与えられた文字列配列を、アナグラム（並び替えで同じになる文字列）ごとにグループ化する問題です。
# 例えば "eat", "tea", "ate" は全て並び替えると "aet" になるので同じグループになります。
#
# 解法:
# 各文字列をソートしたものをキーとして辞書に格納します。
# 既にそのキーが存在すればリストに追加、なければ新規リストを作成します。
# 最後に辞書の値（各グループ）をリストとして返します。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # 文字列をソートしてキーにする
            sorted_s = ''.join(sorted(s))
            # 既存グループに追加 or 新規グループ作成
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        # 辞書の値（グループ）をリストで返す
        return list(anagrams.values())

# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"groupAnagrams({strs}) => {solution.groupAnagrams(strs)}")
