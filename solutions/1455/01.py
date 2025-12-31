from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # For each row, we need the minimum and second minimum
        # to avoid choosing from the same column in adjacent rows
        prev = grid[0][:]

        for i in range(1, n):
            curr = [float("inf")] * n

            # Find min and second min of previous row
            min1, min2 = float("inf"), float("inf")
            idx1 = -1

            for j in range(n):
                if prev[j] < min1:
                    min2 = min1
                    min1 = prev[j]
                    idx1 = j
                elif prev[j] < min2:
                    min2 = prev[j]

            # Calculate current row
            for j in range(n):
                if j == idx1:
                    curr[j] = grid[i][j] + min2
                else:
                    curr[j] = grid[i][j] + min1

            prev = curr

        res = min(prev)
        return res
