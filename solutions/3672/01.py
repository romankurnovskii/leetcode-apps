from typing import List


class Solution:
    def sumWeightedModes(self, nums: List[int]) -> int:
        from collections import Counter

        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i, n):
                subarray = nums[i : j + 1]
                count = Counter(subarray)
                max_freq = max(count.values()) if count else 0

                for num, freq in count.items():
                    if freq == max_freq:
                        res += num * freq

        return res
