class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        max_row = 0

        for i, row in enumerate(mat):
            ones_count = sum(row)
            if ones_count > max_ones:
                max_ones = ones_count
                max_row = i

        return [max_row, max_ones]
