from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        i = 0
        n = len(nums)

        while i < n:
            if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]:
                res += 1
                i += 2
            else:
                i += 1

        return res
