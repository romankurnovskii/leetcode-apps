class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Use Josephus problem solution
        # For 0-indexed: winner = (winner + k) % n
        # Convert to 1-indexed at the end
        winner = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1
