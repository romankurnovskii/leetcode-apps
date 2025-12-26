class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        from functools import lru_cache
        from itertools import product

        m, n = len(grid), len(grid[0])
        res = 0

        @lru_cache(None)
        def dp(i, j, dr):
            # dr = 1 for downward pyramid, dr = -1 for upward pyramid
            if (
                grid[i][j] == 1
                and 0 <= i + dr < m
                and j > 0
                and j + 1 < n
                and grid[i + dr][j] == 1
            ):
                return min(dp(i + dr, j - 1, dr), dp(i + dr, j + 1, dr)) + 1
            return grid[i][j]

        for i, j in product(range(m), range(n)):
            res += max(0, dp(i, j, 1) - 1)  # Downward pyramids
            res += max(0, dp(i, j, -1) - 1)  # Upward pyramids

        return res
