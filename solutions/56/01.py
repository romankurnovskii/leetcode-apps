class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Handle edge case
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Initialize result with first interval
        result = [intervals[0]]

        # Iterate through remaining intervals
        for interval in intervals[1:]:
            # Check if current interval overlaps with last in result
            if interval[0] <= result[-1][1]:
                # Merge intervals by updating end time
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # No overlap, add current interval to result
                result.append(interval)

        # Return merged intervals
        return result
