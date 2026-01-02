from typing import List


class Solution:
    def minCost(self, items: List[List[int]], required: List[int]) -> int:
        from functools import lru_cache

        n = len(required)

        @lru_cache(None)
        def dp(mask):
            if mask == 0:
                return 0

            res = float("inf")
            for item, cost in items:
                new_mask = mask
                for i in range(n):
                    if item[i] > 0:
                        new_mask &= ~(1 << i)

                if new_mask != mask:
                    res = min(res, cost + dp(new_mask))

            return res

        initial_mask = (1 << n) - 1
        res = dp(initial_mask)
        return res if res != float("inf") else -1
