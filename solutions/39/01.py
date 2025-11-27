from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(remaining, combination, start):
            # Base case: if we've reached the target
            if remaining == 0:
                res.append(list(combination))
                return
            
            # If remaining is negative, this path is invalid
            if remaining < 0:
                return
            
            # Try each candidate starting from 'start' to avoid duplicates
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i)
                combination.pop()  # Backtrack
        
        backtrack(target, [], 0)
        return res

