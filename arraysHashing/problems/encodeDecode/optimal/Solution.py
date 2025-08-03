from typing import List

# 問題解説:
# 文字列のリストを1つの文字列に変換（エンコード）し、再び元のリストに戻す（デコード）問題です。
# 区切り文字や特殊文字が含まれていても正しく復元できる方法が必要です。
#
# 解法:
# 各文字列の長さと区切り文字（例: "#"）を使って連結します。
# 例: ["hello", "world"] → "5#hello5#world"
# デコード時は、区切り文字までの数字を長さとして取得し、その長さ分だけ文字列を切り出します。
# これにより、どんな文字列でも安全にエンコード・デコードできます。

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # 長さと区切り文字で連結
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # 区切り文字までの数字が長さ
            i = j + 1
            j = i + length
            res.append(s[i:j])  # 長さ分だけ切り出してリストに追加
            i = j
        return res
# --- 呼び出し例 ---
if __name__ == "__main__":
    solution = Solution()
    strs = ["hello", "world"]
    encoded = solution.encode(strs)
    print(f"encode({strs}) => {encoded}")
    decoded = solution.decode(encoded)
    print(f"decode({encoded}) => {decoded}")
# --- 呼び出し例 ---
# ここでは、strs = ["hello", "world"] をエンコードしてからデコードします。
# 出力は、エンコードされた文字列とデコードされたリストが表示されます。
# 例えば、encode(["hello", "world"]) は "5#hello5#world" のような形式になります。
    solution = Solution()
    strs = ["hello", "world"]
    encoded = solution.encode(strs)
    print(f"encode({strs}) => {encoded}")
    decoded = solution.decode(encoded)
    print(f"decode({encoded}) => {decoded}")
# --- 呼び出し例 ---
# ここでは、strs = ["hello", "world"] をエンコードしてからデコードします。
# 出力は、エンコードされた文字列とデコードされたリストが表示されます。
# 例えば、encode(["hello", "world"]) は "5#hello5#world" のような形式になります。