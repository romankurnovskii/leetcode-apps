from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            # Check bounds and if current cell is land
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return

            # Mark as visited
            grid[i][j] = "0"

            # Explore all 4 directions
            dfs(i - 1, j)  # up
            dfs(i + 1, j)  # down
            dfs(i, j - 1)  # left
            dfs(i, j + 1)  # right

        # Find all islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)

        return res
