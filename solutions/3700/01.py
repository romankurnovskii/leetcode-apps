from typing import List


class Solution:
    def numZigZagArrays(self, nums: List[int], k: int) -> int:
        from functools import lru_cache

        n = len(nums)

        @lru_cache(None)
        def dp(i, prev, direction):
            if i == n:
                return 1 if prev is not None else 0

            res = 0
            for j in range(i, min(i + k, n)):
                if prev is None:
                    res += dp(j + 1, nums[j], 1)
                    res += dp(j + 1, nums[j], -1)
                elif direction == 1:
                    if nums[j] < prev:
                        res += dp(j + 1, nums[j], -1)
                else:
                    if nums[j] > prev:
                        res += dp(j + 1, nums[j], 1)

            return res

        return dp(0, None, 0)
