class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][r] = number of paths to (i,j) with sum % k == r
        # Use 2D DP with k states for remainder
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Initialize starting position
        initial_remainder = grid[0][0] % k
        dp[0][0][initial_remainder] = 1
        
        for i in range(m):
            for j in range(n):
                current_val = grid[i][j]
                
                # Update from top
                if i > 0:
                    for r in range(k):
                        new_remainder = (r + current_val) % k
                        dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i-1][j][r]) % MOD
                
                # Update from left
                if j > 0:
                    for r in range(k):
                        new_remainder = (r + current_val) % k
                        dp[i][j][new_remainder] = (dp[i][j][new_remainder] + dp[i][j-1][r]) % MOD
        
        # Return paths to (m-1, n-1) with remainder 0
        return dp[m-1][n-1][0]

