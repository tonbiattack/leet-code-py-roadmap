from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # res にパスカルの三角形の全行を格納する。初期値として最初の行 [1] を設定
        res = [[1]]

        # rowIndex 行まで繰り返し計算を行う
        for i in range(rowIndex):
            # 現在の最後の行に 0 を前後に追加した配列 temp を作成
            temp = [0] + res[-1] + [0]
            row = []  # 現在の行を格納するリスト

            # 新しい行を計算するループ
            for j in range(len(res[-1]) + 1):
                # 現在の行の各要素は temp の隣り合う要素の和
                row.append(temp[j] + temp[j + 1])
            # 完成した行を res に追加
            res.append(row)

        # 最後に res の最後の行を返す
        return res[-1]


if __name__ == "__main__":
    solution = Solution()

    # テストケース
    rowIndex = 4
    result = solution.getRow(rowIndex)

    # 結果の出力
    print(f"Pascal's Triangle Row {rowIndex}: {result}")
