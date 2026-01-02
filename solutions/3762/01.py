from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        count = Counter(nums)
        res = 0

        for num, freq in count.items():
            if freq < k:
                res += k - freq

        return res
