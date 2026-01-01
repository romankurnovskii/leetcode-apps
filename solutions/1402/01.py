from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        res = 0
        prefix_sum = 0

        for s in satisfaction:
            prefix_sum += s
            if prefix_sum < 0:
                break
            res += prefix_sum

        return res
