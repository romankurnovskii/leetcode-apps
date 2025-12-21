from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Convert nums to a set for O(1) lookup
        nums_set = set(nums)

        # Iterate through positive multiples of k: k, 2k, 3k, ...
        multiple = k
        while True:
            if multiple not in nums_set:
                return multiple
            multiple += k
