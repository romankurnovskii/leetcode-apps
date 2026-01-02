from typing import List


class Solution:
    def maxPartitionFactor(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1

        for i in range(1, n):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i:])

            if right_sum != 0:
                factor = left_sum // right_sum if right_sum > 0 else 0
                res = max(res, factor)

        return res
