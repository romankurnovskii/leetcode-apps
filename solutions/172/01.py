class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0

        # Count factors of 5 (each 5 contributes to a trailing zero)
        # We need to count 5, 25, 125, etc.
        while n > 0:
            n //= 5
            res += n

        return res
