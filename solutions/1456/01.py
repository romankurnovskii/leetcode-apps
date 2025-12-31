from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0])

        # Precompute minimum cost to connect each point in group2
        min_cost2 = [min(cost[i][j] for i in range(size1)) for j in range(size2)]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, mask):
            # i: current index in group1
            # mask: bitmask of connected points in group2

            if i == size1:
                # Connect remaining unconnected points in group2
                res = 0
                for j in range(size2):
                    if not (mask & (1 << j)):
                        res += min_cost2[j]
                return res

            res = float("inf")
            # Try connecting point i to each point in group2
            for j in range(size2):
                res = min(res, cost[i][j] + dp(i + 1, mask | (1 << j)))

            return res

        res = dp(0, 0)
        return res
