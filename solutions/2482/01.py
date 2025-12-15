class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Count ones in each row and column
        ones_row = [0] * m
        ones_col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1

        # Build result matrix
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                zeros_row = n - ones_row[i]
                zeros_col = m - ones_col[j]
                res[i][j] = ones_row[i] + ones_col[j] - zeros_row - zeros_col

        return res
