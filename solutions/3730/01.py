from typing import List


class Solution:
    def maxCalories(self, calories: List[int], k: int) -> int:
        n = len(calories)
        res = 0
        current = 0

        for i in range(n):
            current += calories[i]
            if i >= k:
                current -= calories[i - k]
            res = max(res, current)

        return res
