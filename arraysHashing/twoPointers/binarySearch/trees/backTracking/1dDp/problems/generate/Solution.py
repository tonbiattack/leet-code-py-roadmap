# 解答クラス
from typing import List  # 型ヒントのためのモジュールをインポート

class Solution:
    # generateメソッド: Pascal's Triangleを生成する
    def generate(self, numRows: int) -> List[List[int]]:
        # ベースケース1: 行数が0の場合は空リストを返す
        if numRows == 0:
            # numRowsが0なら、Pascalの三角形は存在しない
            return []  # 空リストを返す
        
        # ベースケース2: 行数が1の場合は単一行を返す
        if numRows == 1:
            # numRowsが1なら、最初の行のみを返す
            return [[1]]  # [[1]]はPascalの三角形の最初の行
        
        # 再帰呼び出し: numRows - 1行までのPascalの三角形を取得
        # 再帰的に生成された「前の行」までの三角形を取得する
        prev_rows = self.generate(numRows - 1)
        
        # 前の行の最後のリストを取得 (Pascalの三角形の直前の行)
        prev_row = prev_rows[-1]  # 例: [1, 3, 3, 1] (4行目の場合)
        
        # 現在の行を初期化。最初の要素は常に1
        current_row = [1]  # 例: [1]
        
        # 現在の行を構築するループ
        # 現在の行の真ん中部分を計算する (2列目から最後の1つ前の列まで)
        for i in range(1, numRows - 1):  # インデックス範囲は1から(numRows-2)まで
            # 前の行の隣接要素を加算
            # 例: prev_row[i - 1] = 3, prev_row[i] = 3 → current_row.append(3 + 3 = 6)
            current_row.append(prev_row[i - 1] + prev_row[i])
        
        # 現在の行の最後の要素は常に1
        current_row.append(1)  # 例: [1, 4, 6, 4, 1]
        
        # 現在の行を全体のリスト (prev_rows) に追加
        prev_rows.append(current_row)  # 例: [[1], [1, 1], ..., [1, 4, 6, 4, 1]]
        
        # 最終的に構築された三角形全体を返す
        return prev_rows  # 全行を含む2次元リストを返す

# メイン部分: このスクリプトが直接実行されたときだけ以下のコードを実行する
if __name__ == "__main__":
    # ソリューションインスタンスを作成
    solution = Solution()

    # Pascal's Triangle を生成する行数を指定
    numRows = 5  # 例: 5行のPascalの三角形を生成

    # メソッドを呼び出して結果を取得
    result = solution.generate(numRows)

    # 結果を出力
    print(result)  # 結果: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
