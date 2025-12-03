class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if it's possible: minimum sum is num (all 1s), maximum is 9*num (all 9s)
        if sum < num or sum > 9 * num:
            return ""
        
        # Greedy: to maximize sum of squares, we want to maximize individual digits
        # Since x^2 grows faster, we want largest digits possible
        # Strategy: fill leftmost positions with 9s, then distribute remaining
        
        digits = []
        remaining_sum = sum
        
        # Fill as many 9s as possible from left to right
        for i in range(num):
            # Can we put a 9 here?
            # Remaining positions: num - i - 1
            # Minimum needed for remaining: num - i - 1 (all 1s)
            # Maximum we can use here: min(9, remaining_sum - (num - i - 1))
            max_digit = min(9, remaining_sum - (num - i - 1))
            if max_digit < 1:
                max_digit = 1
            
            digits.append(str(max_digit))
            remaining_sum -= max_digit
        
        # If there's still remaining sum, we need to distribute it
        # But we already handled this in the loop above
        
        return ''.join(digits)

