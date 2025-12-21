from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j][c] = maximum score at cell (i,j) with total cost exactly c
        # Initialize with -1 to indicate unreachable states
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        # Starting cell (0, 0)
        # Cost: 0 if grid[0][0] == 0, else 1
        # Score: grid[0][0]
        start_cost = 0 if grid[0][0] == 0 else 1
        start_score = grid[0][0]

        if start_cost <= k:
            dp[0][0][start_cost] = start_score

        # Fill the DP table
        for i in range(m):
            for j in range(n):
                # Skip if we're at the starting cell (already initialized)
                if i == 0 and j == 0:
                    continue

                # Calculate cost and score for current cell
                cell_cost = 0 if grid[i][j] == 0 else 1
                cell_score = grid[i][j]

                # Try coming from top (i-1, j)
                if i > 0:
                    for prev_cost in range(k + 1):
                        if dp[i - 1][j][prev_cost] != -1:
                            new_cost = prev_cost + cell_cost
                            if new_cost <= k:
                                new_score = dp[i - 1][j][prev_cost] + cell_score
                                dp[i][j][new_cost] = max(dp[i][j][new_cost], new_score)

                # Try coming from left (i, j-1)
                if j > 0:
                    for prev_cost in range(k + 1):
                        if dp[i][j - 1][prev_cost] != -1:
                            new_cost = prev_cost + cell_cost
                            if new_cost <= k:
                                new_score = dp[i][j - 1][prev_cost] + cell_score
                                dp[i][j][new_cost] = max(dp[i][j][new_cost], new_score)

        # Find maximum score at destination (m-1, n-1) for any cost <= k
        result = -1
        for cost in range(k + 1):
            if dp[m - 1][n - 1][cost] != -1:
                result = max(result, dp[m - 1][n - 1][cost])

        return result
