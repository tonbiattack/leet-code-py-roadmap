from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        文字列リストの中で最長の共通接頭辞を返す。

        Args:
        - strs: 文字列のリスト

        Returns:
        - str: 最長の共通接頭辞。共通接頭辞がない場合は空文字列を返す。
        """
        if not strs:
            return ""

        # 入力リストの中で最も短い文字列を基準とする
        shortest_str = min(strs, key=len)

        # 最長共通接頭辞の長さを探す
        for i, char in enumerate(shortest_str):
            # すべての文字列を比較し、共通しているかチェックする
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]

        return shortest_str


# 例としての呼び出し
solution = Solution()
strs = ["flower", "flow", "flight"]
result = solution.longestCommonPrefix(strs)
print(f"Longest common prefix: {result}")
