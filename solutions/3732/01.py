from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Key insight: Find the two largest absolute values in nums
        # The answer is: max_abs1 * max_abs2 * 10^5
        # We can always make the product positive by choosing the right sign for the replacement

        # Find the two largest absolute values
        max_abs1 = 0
        max_abs2 = 0

        for x in nums:
            abs_x = abs(x)
            if abs_x >= max_abs1:
                max_abs2 = max_abs1
                max_abs1 = abs_x
            elif abs_x > max_abs2:
                max_abs2 = abs_x

        res = max_abs1 * max_abs2 * 100000
        return res
