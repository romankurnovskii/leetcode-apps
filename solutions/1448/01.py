from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False  # Touches boundary

            if grid[i][j] == 1:
                return True  # Water

            grid[i][j] = 1  # Mark as visited

            # Check all 4 directions
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            # Island is closed only if all directions are closed
            return up and down and left and right

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:  # Land
                    if dfs(i, j):
                        res += 1

        return res
