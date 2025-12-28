class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        # Numbers made only of 1s can never be divisible by 2 or 5
        # because they always end in 1 (odd) and never end in 0 or 5
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        # Build the number digit by digit using modulo arithmetic
        # We only need to track the remainder, not the full number
        for i in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return i

        return -1
