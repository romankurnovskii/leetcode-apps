class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # 3D DP: dp[i][j][dir] = number of ways to reach (i,j) with direction dir
        # dir = 0: came from left (moved right to reach here)
        # dir = 1: came from above (moved down to reach here)
        dp = [[[-1, -1] for _ in range(n)] for _ in range(m)]

        def dfs(i, j, dir):
            # Base case: reached destination
            if i == m - 1 and j == n - 1:
                return 1

            # Out of bounds
            if i >= m or j >= n:
                return 0

            # Memoization
            if dp[i][j][dir] != -1:
                return dp[i][j][dir]

            res = 0

            # If current cell is a mirror
            if grid[i][j] == 1:
                if dir == 0:  # Came from left, reflect down
                    res = dfs(i + 1, j, 1)
                else:  # dir == 1, came from above, reflect right
                    res = dfs(i, j + 1, 0)
            else:
                # Not a mirror, can move both right and down
                # Move right
                res = (res + dfs(i, j + 1, 0)) % MOD
                # Move down
                res = (res + dfs(i + 1, j, 1)) % MOD

            dp[i][j][dir] = res
            return res

        # Start at (0,0). Since grid[0][0] is always 0 (not a mirror), we can start with dir=0
        # The dir parameter represents the direction we came from, but at start it's arbitrary
        # Since (0,0) is not a mirror, we'll try both moves anyway
        return dfs(0, 0, 0) % MOD
