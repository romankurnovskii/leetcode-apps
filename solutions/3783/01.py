class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Reverse the digits of n
        reversed_n = int(str(n)[::-1])

        # Return absolute difference
        return abs(n - reversed_n)
