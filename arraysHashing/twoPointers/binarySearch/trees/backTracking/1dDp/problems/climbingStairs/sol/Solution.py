class Solution:
    # メソッドの定義。nは登る段数。
    def climbStairs(self, n: int) -> int:
        # 階段が0段または1段の場合、そのままnが答え。
        if n <= 1:
            return n

        # 初期値の設定
        # num1 は前々回の階段の登り方の数
        # num2 は前回の階段の登り方の数
        num1, num2 = 0, 1

        # ループで階段の登り方を計算
        # 0からn-1まで反復
        for i in range(n):
            # num2に新しい合計、num1に古いnum2を更新
            num1, num2 = num2, num1 + num2

        # num2に最終結果が格納されている
        return num2

# メイン関数が呼び出しの起点
if __name__ == "__main__":
    # Solution クラスのインスタンス化
    solution = Solution()
    
    # 段数を指定して関数を呼び出し
    # 例: n=3 の場合
    result = solution.climbStairs(3)
    
    # 結果を出力
    # この場合、結果は 3 が出力される (1+1+1, 1+2, 2+1)
    print(result)
