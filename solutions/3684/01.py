from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # Get distinct elements by converting to set
        distinct = list(set(nums))
        
        # Sort in descending order to get largest elements first
        distinct.sort(reverse=True)
        
        # Take at most k elements
        res = distinct[:k]
        
        return res

