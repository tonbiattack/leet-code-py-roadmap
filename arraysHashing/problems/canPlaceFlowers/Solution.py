from typing import List

class Solution:
    """
    Solutionクラスは、花壇に花を植えることができるかを判断するメソッドを提供します。

    メソッド:
    canPlaceFlowers(flowerbed: List[int], n: int) -> bool
        与えられた花壇flowerbedに、n本の花を植えることができるかどうかを判定します。

    アルゴリズムの概要:
    - 連続する場所に花を植えることはできないため、flowerbedの各インデックスを順に確認します。
    - 現在のインデックスが0で、前後の位置に花が植えられていない場合、花を植え、nを1減らします。
    - nが0になった時点で、Trueを返します。最終的にnが0にならなければFalseを返します。

    パラメータ:
    flowerbed (List[int]): 花壇の状態を表す配列（0は空き、1は既に花が植えられている）。
    n (int): 植える予定の花の本数。

    戻り値:
    bool: 花をn本植えることが可能かどうか。
    """

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            # 現在の場所 flowerbed[i] が空であり、前後にも花がない場合
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                # 花を植える
                flowerbed[i] = 1
                n -= 1
                # 全ての花を植えた場合はTrueを返す
                if n == 0:
                    return True
        # n本の花を全て植えることができなかった場合はFalseを返す
        return False

# 呼び出し例
if __name__ == "__main__":
    solution = Solution()
    
    # テストケース1: flowerbed = [1, 0, 0, 0, 1], n = 1
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    print(solution.canPlaceFlowers(flowerbed1, n1))  # Expected: True

    # テストケース2: flowerbed = [1, 0, 0, 0, 1], n = 2
    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    print(solution.canPlaceFlowers(flowerbed2, n2))  # Expected: False

    # テストケース3: flowerbed = [0, 0, 1, 0, 0], n = 1
    flowerbed3 = [0, 0, 1, 0, 0]
    n3 = 1
    print(solution.canPlaceFlowers(flowerbed3, n3))  # Expected: True
