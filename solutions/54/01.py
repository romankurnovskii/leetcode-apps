class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Handle edge case
        if not matrix:
            return []

        # Initialize boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []

        # Traverse in spiral order
        while top <= bottom and left <= right:
            # Traverse right (top row)
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse down (right column)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse left (bottom row) - check if still valid
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse up (left column) - check if still valid
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        # Return the spiral order
        return result
