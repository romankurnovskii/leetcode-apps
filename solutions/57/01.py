class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Initialize result list
        result = []

        # Add intervals that end before new interval starts
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            else:
                break

        # Merge overlapping intervals
        start, end = newInterval[0], newInterval[1]
        for interval in intervals:
            if interval[0] <= end and interval[1] >= start:
                # Overlap found, update boundaries
                start = min(start, interval[0])
                end = max(end, interval[1])
            elif interval[0] > end:
                # No more overlaps, add merged interval and remaining intervals
                result.append([start, end])
                result.extend(intervals[intervals.index(interval) :])
                return result

        # Add the final merged interval
        result.append([start, end])

        # Return result
        return result
