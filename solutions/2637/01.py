from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        max_row = -1
        
        for i, row in enumerate(mat):
            ones = sum(row)
            if ones > max_ones:
                max_ones = ones
                max_row = i
        
        return [max_row, max_ones]
