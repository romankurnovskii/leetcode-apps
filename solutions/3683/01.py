class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        # Calculate finish time for each task: start_time + duration
        # Return the minimum finish time
        res = float("inf")

        for start, duration in tasks:
            finish_time = start + duration
            res = min(res, finish_time)

        return res
