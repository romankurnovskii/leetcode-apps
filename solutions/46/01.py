from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(current):
            # Base case: if we've used all numbers
            if len(current) == len(nums):
                res.append(list(current))
                return
            
            # Try each unused number
            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()  # Backtrack
        
        backtrack([])
        return res

