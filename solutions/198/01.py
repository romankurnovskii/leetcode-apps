from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # dp[i] represents maximum money robbed up to house i
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill dp array
        for i in range(2, n):
            # Either rob current house + best from i-2, or skip current house
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]
