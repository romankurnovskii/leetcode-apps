class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Josephus problem
        # Use 0-indexed, then convert to 1-indexed at the end
        res = 0
        for i in range(2, n + 1):
            res = (res + k) % i
        return res + 1
