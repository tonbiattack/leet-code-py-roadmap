from typing import List


# 問題解説:# 文字列のリストをエンコードして1つの文字列に変換し、
# その文字列をデコードして元のリストに戻す問題です。
# 例えば ["hello", "world"] をエンコードすると "5#hello5#world" のようになります。
# エンコードでは各文字列の長さと内容を結合し、デコードではその形式を解析して元の文字列に戻します。
# この方法は、文字列の長さを明示的に含めることで、デコード時に正確に文字列を再構築できるようにしています。
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        # 解説: エンコードされた文字列を解析して元のリストに戻す
        # 文字列の長さを示す部分を見つけて、その後の文字列を抽出します
        while i < len(s):
            # 解説: '#' の位置を見つけて、長さを取得
            # 文法解説: s.index('#', i) は、i から始まる最初の '#' の位置を返します
            j = s.index('#', i)
            # 文法解説: s[i:j] は、i から j までの部分文字列を取得します
            # 文字列の長さを取得
            # 文法解説: int(s[i:j]) は、文字列を整数に変換します
            length = int(s[i:j])
            # 文法解説: s[j+1:j+1+length] は、j+1 から j+1+length までの部分文字列を取得します
            # 文字列を抽出してリストに追加
            decoded.append(s[j+1:j+1+length])
            # 文法解説: i = j + 1 + length は、次の文字列の開始位置を更新します
            # ここで j は '#' の位置、length は文字列の長さなので、次の文字列は j+1 から始まります
            i = j + 1 + length
        return decoded
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