from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            if j - i > 1:
                segment_costs = cost[i:j]
                segment_costs.sort()
                res += sum(segment_costs[:-1])

            i = j

        return res
