class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        # Count ones in each row and column
        onesRow = [0] * m
        onesCol = [0] * n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
        
        # Build result matrix
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            zerosRow = n - onesRow[i]
            for j in range(n):
                zerosCol = m - onesCol[j]
                res[i][j] = onesRow[i] + onesCol[j] - zerosRow - zerosCol
        
        return res
