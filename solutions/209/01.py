from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float('inf')
        current_sum = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                res = min(res, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0

