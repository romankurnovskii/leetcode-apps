from bisect import bisect_left, bisect_right


class ExamTracker:
    def __init__(self):
        self.times = []
        self.scores = []
        self.prefix_sum = [0]  # prefix_sum[i] = sum of scores[0:i]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.scores.append(score)
        # Update prefix sum
        self.prefix_sum.append(self.prefix_sum[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        # Find the range of indices in times array
        # Find left bound: first index where times[i] >= startTime
        left = bisect_left(self.times, startTime)
        # Find right bound: first index where times[i] > endTime
        right = bisect_right(self.times, endTime)

        if left >= right:
            return 0

        # Sum of scores from left to right-1
        return self.prefix_sum[right] - self.prefix_sum[left]
