from typing import List


class Solution:
    def sumOfPerfectSquares(self, nums: List[int]) -> int:
        def is_perfect_square(n):
            root = int(n**0.5)
            return root * root == n

        n = len(nums)
        res = 0

        for i in range(n):
            if is_perfect_square(nums[i]):
                for j in range(i):
                    if is_perfect_square(nums[j]):
                        res += nums[i]

        return res
