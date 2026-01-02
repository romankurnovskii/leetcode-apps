from typing import List


class Solution:
    def sumWeightedModes(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        max_freq = max(count.values()) if count else 0

        res = 0
        for num, freq in count.items():
            if freq == max_freq:
                res += num * freq

        return res
