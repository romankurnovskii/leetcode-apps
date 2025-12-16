class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Josephus problem - 1-indexed
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1
