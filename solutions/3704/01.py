from typing import List


class Solution:
    def countPairs(self, nums: List[int], n: int) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] != 0 and nums[j] != 0 and nums[i] + nums[j] == n:
                    res += 1

        return res
