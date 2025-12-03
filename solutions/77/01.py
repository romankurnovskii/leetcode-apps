from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, current_combination):
            # Base case: combination of size k found
            if len(current_combination) == k:
                res.append(current_combination[:])
                return
            
            # Try each number from start to n
            for i in range(start, n + 1):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Backtrack
        
        backtrack(1, [])
        return res

