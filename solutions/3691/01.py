from typing import List


class Solution:
    def maxSubarrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")

        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]
                res = max(res, current)

        return res
