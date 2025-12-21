from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # dp[i] represents minimum cost to reach step i
        dp = [0] * (n + 1)

        # Base cases: can start at step 0 or step 1 with cost 0
        dp[0] = 0
        dp[1] = 0

        # Fill dp array
        for i in range(2, n + 1):
            # Can reach step i from step i-1 or step i-2
            # Add the cost of the step we're leaving
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]
