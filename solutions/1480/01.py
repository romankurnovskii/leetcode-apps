from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            res.append(current_sum)
        
        return res

