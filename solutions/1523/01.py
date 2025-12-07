class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count of numbers in range [low, high]
        total = high - low + 1
        
        # If total is even, exactly half are odd
        if total % 2 == 0:
            return total // 2
        
        # If total is odd, check if low is odd
        # If low is odd, we have one more odd than even
        return total // 2 + (1 if low % 2 == 1 else 0)

