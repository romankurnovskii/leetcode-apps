from typing import List


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i, n):
                subarray = nums[i : j + 1]
                if len(set(subarray)) == 1:
                    res += 1

        return res
