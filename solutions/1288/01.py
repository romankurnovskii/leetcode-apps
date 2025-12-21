class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start (ascending), then by end (descending)
        # This ensures that if two intervals have same start, wider one comes first
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        max_end = -1

        for start, end in intervals:
            # If current interval is not covered
            if end > max_end:
                res += 1
                max_end = end

        return res
