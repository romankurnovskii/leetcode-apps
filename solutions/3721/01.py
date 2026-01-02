from typing import List


class Solution:
    def longestBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            count0 = 0
            count1 = 0
            for j in range(i, n):
                if nums[j] == 0:
                    count0 += 1
                else:
                    count1 += 1

                if count0 == count1:
                    res = max(res, j - i + 1)

        return res
