from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j] represents minimum path sum to reach (i, j)
        dp = [[0] * n for _ in range(m)]

        # Base case: starting position
        dp[0][0] = grid[0][0]

        # Fill first row: can only come from left
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill first column: can only come from top
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                # Can come from top or left, choose minimum
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]
