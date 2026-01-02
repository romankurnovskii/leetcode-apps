from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        res = 0
        for i in range(1, n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n] - prefix_sum[i]
            res = max(res, left_sum + right_sum)

        return res
