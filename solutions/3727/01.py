from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Since we can rearrange, we want to maximize the alternating sum
        # The pattern is: +a^2 - b^2 + c^2 - d^2 + ...
        # We need to assign numbers to positive (even index) and negative (odd index) positions
        # To maximize: put largest squares in positive positions, smallest squares in negative positions
        
        n = len(nums)
        squares = [x * x for x in nums]
        squares.sort(reverse=True)
        
        # Count how many positive and negative positions we have
        num_positive = (n + 1) // 2  # Even indices: 0, 2, 4, ...
        num_negative = n // 2  # Odd indices: 1, 3, 5, ...
        
        # Assign largest squares to positive positions, smallest to negative
        res = sum(squares[:num_positive]) - sum(squares[num_positive:])
        
        return res
