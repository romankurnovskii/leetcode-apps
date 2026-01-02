from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mod0 = []
        mod1 = []
        mod2 = []

        for num in nums:
            if num % 3 == 0:
                mod0.append(num)
            elif num % 3 == 1:
                mod1.append(num)
            else:
                mod2.append(num)

        mod0.sort(reverse=True)
        mod1.sort(reverse=True)
        mod2.sort(reverse=True)

        res = -1

        if len(mod0) >= 3:
            res = max(res, mod0[0] + mod0[1] + mod0[2])

        if len(mod1) >= 3:
            res = max(res, mod1[0] + mod1[1] + mod1[2])

        if len(mod2) >= 3:
            res = max(res, mod2[0] + mod2[1] + mod2[2])

        if len(mod0) >= 1 and len(mod1) >= 1 and len(mod2) >= 1:
            res = max(res, mod0[0] + mod1[0] + mod2[0])

        return res
