# このコードは、整数 x の整数平方根を計算する問題を解いています。整数平方根とは、√x の整数部分を求めることです。
# たとえば、x = 8 の場合、√8 ≈ 2.828 なので、整数部分である 2 が返されます。
class Solution:
    def mySqrt(self, x: int) -> int:
        # もし x が 0 なら、その平方根も 0 なので 0 を返します。
        if x == 0:
            return 0

        # 二分探索の開始位置を 1 に、終了位置を x に設定します。
        first, last = 1, x

        # 二分探索のループを開始します。first が last 以下の間、探索を続けます。
        while first <= last:
            # 中央値 mid を計算。first と last の中間位置です。
            mid = first + (last - first) // 2

            # x // mid は x を mid で割った商（整数除算）です。
            # もし mid が x // mid と等しい場合、mid は整数平方根です。
            if mid == x // mid:
                return mid

            # mid が x // mid より大きい場合、mid は平方根の候補として大きすぎるため
            # last を mid - 1 に設定し、探索範囲を左側（小さい方）に絞ります。
            elif mid > x // mid:
                last = mid - 1

            # mid が x // mid より小さい場合、mid はまだ小さいため
            # first を mid + 1 に設定し、探索範囲を右側（大きい方）に絞ります。
            else:
                first = mid + 1

        # ループを抜けた時点で、last は整数平方根の最大の候補値です。
        # これを返すことで、`√x` の整数部分を得ます。
#         ループ終了後の last の意味

# 二分探索ループを抜けると、first が last よりも大きくなります。
# この時点で、last は x 以下の最大の整数で、その数の2乗がx以下 の条件を満たしています。
# したがって、last を返すことで、√x の整数部分が得られるのです。
        return last
