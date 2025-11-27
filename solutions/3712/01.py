from typing import List
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        # Count frequency of each element
        freq = Counter(nums)
        
        res = 0
        
        # For each element, if its frequency is divisible by k,
        # add the element * frequency to the sum
        for num, count in freq.items():
            if count % k == 0:
                res += num * count
        
        return res

