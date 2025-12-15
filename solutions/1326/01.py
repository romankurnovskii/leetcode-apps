class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Create intervals
        intervals = []
        for i in range(n + 1):
            if ranges[i] > 0:
                left = max(0, i - ranges[i])
                right = min(n, i + ranges[i])
                intervals.append((left, right))

        if not intervals:
            return -1

        # Sort by left endpoint
        intervals.sort()

        res = 0
        covered = 0
        i = 0

        while covered < n:
            max_right = covered
            # Find interval that starts <= covered and extends farthest
            while i < len(intervals) and intervals[i][0] <= covered:
                max_right = max(max_right, intervals[i][1])
                i += 1

            if max_right == covered:
                return -1  # Cannot extend coverage

            covered = max_right
            res += 1

        return res
