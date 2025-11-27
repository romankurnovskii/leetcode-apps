from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(index, current_subset):
            # Add current subset to result
            res.append(current_subset[:])
            
            # Try adding each remaining element
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
        
        backtrack(0, [])
        return res

