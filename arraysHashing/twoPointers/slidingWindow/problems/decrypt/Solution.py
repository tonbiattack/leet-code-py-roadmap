# この問題「Defuse the Bomb」は、配列の要素を使って新しい配列を生成する操作を求める問題です。以下に問題の内容を日本語で解説します。

# 問題概要
# セキュリティの観点から配列の要素に基づき、新しい配列を作成していく問題です。

# 入力
# code: 整数のリスト。各要素が暗号コードの一部を表しています。
# k: 整数。新しい配列を生成するためのキーとして使用されます。
# 処理
# この問題では、新しい配列resを生成します。各要素res[i]は、以下のルールに従ってcodeの要素を基に計算されます。

# k > 0の場合：res[i]はcode[i]の次のk個の要素の合計になります。
# k < 0の場合：res[i]はcode[i]の前の|k|個の要素の合計になります。
# k == 0の場合：res[i]は必ず0になります。
# 注意
# code配列は円形（循環）として扱われます。したがって、リストの終端に到達した場合には、最初に戻って次の要素を参照することができます。

# 例
# 入力例 1
# plaintext
# コードをコピーする
# code = [5, 7, 1, 4]
# k = 3
# k > 0なので、res[i]は各要素の次の3個の要素の合計です。
# res[0] = code[1] + code[2] + code[3] = 7 + 1 + 4 = 12
# res[1] = code[2] + code[3] + code[0] = 1 + 4 + 5 = 10
# res[2] = code[3] + code[0] + code[1] = 4 + 5 + 7 = 16
# res[3] = code[0] + code[1] + code[2] = 5 + 7 + 1 = 13
# 結果：

# plaintext
# コードをコピーする
# res = [12, 10, 16, 13]
# 入力例 2
# plaintext
# コードをコピーする
# code = [2, 4, 9, 3]
# k = -2
# k < 0なので、res[i]は各要素の前の2個の要素の合計です。
# res[0] = code[2] + code[3] = 9 + 3 = 12
# res[1] = code[3] + code[0] = 3 + 2 = 5
# res[2] = code[0] + code[1] = 2 + 4 = 6
# res[3] = code[1] + code[2] = 4 + 9 = 13
# 結果：

# plaintext
# コードをコピーする
# res = [12, 5, 6, 13]
# ポイント
# 配列の要素を円形に参照すること。
# kの符号によって処理が変わる点。
# k == 0の場合には、新しい配列はすべて0になる点。
# この問題を解くには、リストのスライスやインデックスの計算を活用する必要があります。
from typing import List


class Solution:
    # decryptメソッドを定義
    # このメソッドは整数のリスト code と整数 k を引数にとり、整数のリストを返します。
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # kが0の場合、リスト全体を0で埋めたリストを返します。
        # 0が代入されるのは、各要素が影響を受けないようにするためです。
        if k == 0:
            # リスト内包表記を使ってcodeと同じ長さのリストを作成し、すべての要素を0にします。
            return [0 for i in code]

        # 元のcodeリストをtempに代入
        # tempには、最終的な計算結果が格納されます。
        temp = code

        # codeリストを2回繰り返した新しいリストを作成し、再度codeに代入
        # これによりリストが「円環」（ループ）として扱いやすくなります。
        # 例えばcodeが[5, 7, 1, 4]の場合、[5, 7, 1, 4, 5, 7, 1, 4]のように展開されます。
        code = code * 2

        # tempリストの各インデックスiに対して処理を行います。
        # len(temp)は元のcodeリストの長さで、全要素に対する処理を一度ずつ行います。
        for i in range(len(temp)):
            # kが正の数の場合の処理
            # code[i + 1 : i + k + 1]は、現在の要素iの「次の」k個の要素を切り出します。
            if k > 0:
                # 切り出した要素の合計を計算し、temp[i]に格納します。
                # これによりtemp[i]には「次のk個」の要素の合計が代入されます。
                temp[i] = sum(code[i + 1: i + k + 1])
            # kが負の数の場合の処理
            # code[i + len(temp) + k : i + len(temp)]は、現在の要素iの「前の」|k|個の要素を切り出します。
            else:
                # 切り出した要素の合計を計算し、temp[i]に格納します。
                # これによりtemp[i]には「前の|k|個」の要素の合計が代入されます。
                temp[i] = sum(code[i + len(temp) + k: i + len(temp)])

        # 最終的な計算結果が格納されたtempリストを返します。
        return temp


        # Solutionクラスのインスタンスを作成し、テストケースでメソッドを呼び出して出力
sol = Solution()
# print(sol.decrypt([5, 7, 1, 4], 3))
print(sol.decrypt([2, 4, 9, 3], -2))
