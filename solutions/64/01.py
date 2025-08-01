class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Handle edge case
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        # Initialize DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        # Return result
        return dp[m - 1][n - 1]
