from typing import List

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        has_even = False
        
        for num in nums:
            if num % 2 == 0:
                # Even number: perform bitwise OR
                result |= num
                has_even = True
        
        return result if has_even else 0

