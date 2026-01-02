from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        from collections import Counter

        count = Counter(nums)
        distinct = sorted(count.keys(), reverse=True)

        res = 0
        used = 0

        for num in distinct:
            freq = min(count[num], k - used)
            res += num * freq
            used += freq
            if used >= k:
                break

        return res
