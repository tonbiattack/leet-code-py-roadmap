from typing import List  # 型ヒント用のListをインポート

# 問題解説:
# 配列の各要素について「その要素以外の全ての積」を求める問題です。
# 例えば [1,2,3,4] なら、出力は [2*3*4, 1*3*4, 1*2*4, 1*2*3] → [24,12,8,6] となります。
#
# 解法:
# 1. 各要素の左側の積を answer[i] に格納（左から順に計算）
# 2. 各要素の右側の積を answer[i] に掛け合わせる（右から順に計算）
# これにより、除外したい要素以外の積が効率よく求まります。
# 追加配列を使わずO(n)時間・O(1)空間で解けます。

class Solution:  # 問題を解くためのクラス定義
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # メイン関数。引数numsは整数リスト、戻り値も整数リスト
        length = len(nums)  # 配列の長さを取得
        answer = [1] * length   # 結果格納用リスト。全要素を1で初期化

        # 左側の積を計算
        left_product = 1  # 左側の積の初期値
        for i in range(length):  # 0からlength-1までループ
            answer[i] = left_product  # 現在の左積を格納
            left_product *= nums[i]   # 左積を更新（次の要素用）

        # 右側の積を掛け合わせる
        right_product = 1  # 右側の積の初期値
        # 文法的に、逆順ループを使って右側の積を計算
        # range(開始, 終了(含まない), ステップ) の形。ここでは length-1 から 0 まで 1ずつ減らす。
        # 例: range(3, -1, -1) → [3, 2, 1, 0]
        for i in range(length - 1, -1, -1):  # length-1から0まで逆順ループ
            answer[i] *= right_product  # 右積を掛け合わせる
            right_product *= nums[i]    # 右積を更新（次の要素用）

        return answer  # 結果リストを返す

# --- 呼び出し例 ---
if __name__ == "__main__":  # このファイルが直接実行された場合のみ実行
    solution = Solution()    # Solutionクラスのインスタンス作成
    nums = [1, 2, 3, 4]      # 入力例
    result = solution.productExceptSelf(nums)  # 関数呼び出し
    print(f"productExceptSelf({nums}) => {result}")  # 結果表示
