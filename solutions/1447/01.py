from typing import List


class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        n = len(colsum)
        res = [[0] * n, [0] * n]

        # First pass: handle columns with sum 2 or 0
        for j in range(n):
            if colsum[j] == 2:
                res[0][j] = 1
                res[1][j] = 1
                upper -= 1
                lower -= 1
            elif colsum[j] == 0:
                res[0][j] = 0
                res[1][j] = 0

        # Check if we have enough ones
        if upper < 0 or lower < 0:
            return []

        # Second pass: handle columns with sum 1
        for j in range(n):
            if colsum[j] == 1:
                if upper > 0:
                    res[0][j] = 1
                    upper -= 1
                elif lower > 0:
                    res[1][j] = 1
                    lower -= 1
                else:
                    return []

        # Check if we used all ones
        if upper != 0 or lower != 0:
            return []

        return res
