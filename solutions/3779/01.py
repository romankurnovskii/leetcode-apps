from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        res = 0

        for freq in count.values():
            if freq == 1:
                return -1

            res += (freq + 2) // 3

        return res
