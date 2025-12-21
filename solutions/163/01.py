from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower - 1

        for num in nums + [upper + 1]:
            if num - prev == 2:
                res.append(str(prev + 1))
            elif num - prev > 2:
                res.append(f"{prev + 1}->{num - 1}")
            prev = num

        return res
