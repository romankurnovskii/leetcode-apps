class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle edge cases
        if x == 0 or x == 1:
            return x

        # Binary search
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2

            # Check if mid * mid <= x
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid - 1

        # Return the largest value where k² ≤ x
        return right
