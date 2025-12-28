class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, res = m - 1, 0, 0

        # Start from bottom-left corner
        # Trace the outline of the "staircase" of negative numbers
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                # All elements to the right in this row are negative
                res += n - c
                r -= 1  # Move up
            else:
                c += 1  # Move right

        return res
