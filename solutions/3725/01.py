from typing import List
import math


class Solution:
    def countWays(self, grid: List[List[int]]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def coprime(a, b):
            return gcd(a, b) == 1

        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                for x in range(m):
                    for y in range(n):
                        if (i, j) != (x, y) and coprime(grid[i][j], grid[x][y]):
                            res += 1

        return res // 2
