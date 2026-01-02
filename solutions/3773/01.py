from typing import List


class Solution:
    def maxRuns(self, nums: List[int]) -> int:
        from collections import defaultdict

        n = len(nums)
        res = 0

        for length in range(1, n + 1):
            count = defaultdict(int)
            for i in range(n - length + 1):
                subarray = tuple(nums[i : i + length])
                count[subarray] += 1
                res = max(res, count[subarray])

        return res
