class Solution:
    def isValid(self, s: str) -> bool:
        # スタックの初期化
        stack = []

        # 閉じ括弧と対応する開き括弧のマッピングを定義
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # 文字列を1文字ずつ処理
        for c in s:
            # 文字が閉じ括弧である場合
            if c in closeToOpen:
                # スタックが空でないかつスタックのトップが対応する開き括弧であれば、スタックから取り出す
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # 対応する開き括弧でない場合、文字列は不正
                else:
                    return False
            # 文字が開き括弧である場合、スタックに追加
            else:
                stack.append(c)

        # スタックが空なら全ての括弧が対応しているためTrueを返す
        return True if not stack else False


# Solutionクラスのインスタンスを作成
sol = Solution()

# テストケースを定義
print(sol.isValid("[]"))        # 出力: True
# print(sol.isValid("([{}])"))    # 出力: True
print(sol.isValid("[(])"))      # 出力: False
print(sol.isValid("{[()]}"))    # 出力: True
print(sol.isValid("{[(])}"))    # 出力: False
