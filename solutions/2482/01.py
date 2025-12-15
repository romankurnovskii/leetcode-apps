from typing import List

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
        res = []
        for i in range(m):
            row = []
            for j in range(n):
                zerosRow = n - onesRow[i]
                zerosCol = m - onesCol[j]
                diff = onesRow[i] + onesCol[j] - zerosRow - zerosCol
                row.append(diff)
            res.append(row)
        
        return res
