from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        result = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                # Even index: add
                result += num
            else:
                # Odd index: subtract
                result -= num
        return result

