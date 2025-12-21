from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Binary search on the flattened matrix
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
