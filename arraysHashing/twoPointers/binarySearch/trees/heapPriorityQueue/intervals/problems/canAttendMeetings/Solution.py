# 会議の時間を表すIntervalクラスの定義
from typing import List


class Interval(object):
    def __init__(self, start, end):
        # 開始時間をstart属性にセット
        self.start = start
        # 終了時間をend属性にセット
        self.end = end

# ソリューションのクラス
class Solution:
    # canAttendMeetingsメソッドは、与えられた会議のスケジュールを受け取り、
    # すべての会議に参加できるかどうかを真偽値で返します。
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 1. 会議を開始時間順にソートします。
        # 各会議の開始時間に基づいて昇順でソートします。
        intervals.sort(key=lambda i: i.start)

        # 2. ソートした会議のリストを順に確認します。
        # 会議が重ならないかを確認するために、隣接する会議の終了時間と開始時間を比較します。
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # 前の会議
            i2 = intervals[i]      # 現在の会議

            # 3. 会議が重なるかを確認します。
            # 前の会議の終了時間が現在の会議の開始時間より後の場合、重なりが発生しています。
            if i1.end > i2.start:
                return False  # 会議が重なる場合、すべての会議に出席できないのでFalseを返す

        # 4. 全ての会議が重ならなかった場合はTrueを返します。
        # 重なりがない場合、すべての会議に出席できると判断します。
        return True

# 呼び出し部分のコード
# 各会議の開始時間と終了時間を指定してIntervalオブジェクトを作成し、リストに格納します。
meetings = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

# Solutionクラスのインスタンスを作成します。
solution = Solution()

# canAttendMeetingsメソッドを呼び出して、全ての会議に出席できるかどうかを確認します。
# 期待する出力は False です（なぜなら会議が重なっているため）。
result = solution.canAttendMeetings(meetings)

# 結果を出力
print(result)  # False
