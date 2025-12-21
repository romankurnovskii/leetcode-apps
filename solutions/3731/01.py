from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Find the minimum and maximum values
        min_val = min(nums)
        max_val = max(nums)

        # Convert nums to a set for O(1) lookup
        nums_set = set(nums)

        # Find all missing elements in the range [min_val, max_val]
        missing = []
        for num in range(min_val + 1, max_val):
            if num not in nums_set:
                missing.append(num)

        return missing
