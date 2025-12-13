from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Calculate maximum OR (OR of all elements)
        max_or = 0
        for num in nums:
            max_or |= num
        
        res = 0
        n = len(nums)
        
        # Generate all subsets using bitmask
        for mask in range(1, 1 << n):
            current_or = 0
            for i in range(n):
                if mask & (1 << i):
                    current_or |= nums[i]
            
            if current_or == max_or:
                res += 1
        
        return res

