from typing import List


class Solution:
    def numZigZagArrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        res = 0

        for i in range(n - 1):
            if (i % 2 == 0 and nums[i] < nums[i + 1]) or (
                i % 2 == 1 and nums[i] > nums[i + 1]
            ):
                res += 1

        return res + 1
