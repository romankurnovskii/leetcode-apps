from typing import List


class Solution:
    def maxXOR(self, nums: List[int]) -> int:
        from functools import lru_cache

        n = len(nums)

        @lru_cache(None)
        def dp(i, xor_val):
            if i == n:
                return xor_val

            return max(dp(i + 1, xor_val), dp(i + 1, xor_val ^ nums[i]))

        return dp(0, 0)
