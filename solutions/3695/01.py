from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], k: int) -> int:
        from functools import lru_cache

        n = len(nums)

        @lru_cache(None)
        def dp(i, swapped, used):
            if used == k:
                return 0
            if i == n:
                return float("-inf")

            res = dp(i + 1, swapped, used)

            if not swapped:
                res = max(res, nums[i] + dp(i + 1, True, used))
            else:
                res = max(res, -nums[i] + dp(i + 1, False, used + 1))

            return res

        return dp(0, False, 0)
