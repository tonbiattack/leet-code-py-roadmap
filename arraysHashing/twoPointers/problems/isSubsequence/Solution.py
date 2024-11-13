# サブシーケンスチェックのための関数
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # sの長さがtより大きければ、sがtのサブシーケンスになることはありえないため、Falseを返す
        if len(s) > len(t):
            return False

        # sが空文字列の場合、tのどの文字列にもサブシーケンスとみなされるのでTrueを返す
        if len(s) == 0:
            return True

        # subsequenceはs内の現在確認している文字のインデックスを追跡する変数
        subsequence = 0

        # tの全ての文字を順にチェックするためのループ
        for i in range(0, len(t)):
            # 現在のサブシーケンスインデックスがsの範囲内かどうかをチェック
            if subsequence <= len(s) - 1:
                # デバッグ用に現在のsのサブシーケンスの文字を表示
                print(s[subsequence])

                # sの現在の文字とtの現在の文字が一致する場合、次の文字を確認するためにインデックスを1つ進める
                if s[subsequence] == t[i]:
                    subsequence += 1

        # sの全ての文字が一致した場合、subsequenceのインデックスはsの長さと等しくなるためTrueを返す
        # そうでない場合はFalseを返す
        return subsequence == len(s)

# Solutionクラスのインスタンスを作成
solution = Solution()

# sがtのサブシーケンスかどうかを確認
s = "abc"  # チェック対象のサブシーケンス
t = "ahbgdc"  # チェックする文字列

# 結果の出力
result = solution.isSubsequence(s, t)
print(f"Is '{s}' a subsequence of '{t}'? -> {result}")
