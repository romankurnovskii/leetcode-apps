from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            min_sum = min(min_sum, prefix_sum)

        res = 1 - min_sum
        return res
