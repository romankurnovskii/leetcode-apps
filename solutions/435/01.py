from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        
        # Count of intervals to remove
        res = 0
        
        # Track the end time of the last kept interval
        last_end = float('-inf')
        
        # Iterate through sorted intervals
        for start, end in intervals:
            # If current interval doesn't overlap with last kept interval
            if start >= last_end:
                # Keep this interval
                last_end = end
            else:
                # Overlap detected, remove current interval
                res += 1
        
        return res


