from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # First pass: calculate left products
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Second pass: calculate right products and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res
