class Solution:
    def climbStairs(self, n: int) -> int:
        # Handle base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize variables for Fibonacci sequence
        prev, curr = 1, 2

        # Iterate from step 3 to step n
        for i in range(3, n + 1):
            # Calculate next value
            next_val = prev + curr

            # Update variables
            prev, curr = curr, next_val

        # Return the number of ways to reach step n
        return curr
