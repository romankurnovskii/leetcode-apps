from typing import List
from collections import defaultdict


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        # Try all possible subarrays
        for i in range(n):
            even_set = set()
            odd_set = set()

            for j in range(i, n):
                # Add current number to appropriate set
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])

                # Check if balanced (equal number of distinct even and odd)
                if len(even_set) == len(odd_set):
                    res = max(res, j - i + 1)

        return res
