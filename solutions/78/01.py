from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, current):
            # Add current subset
            res.append(list(current))
            
            # Try adding each remaining number
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()  # Backtrack
        
        backtrack(0, [])
        return res

