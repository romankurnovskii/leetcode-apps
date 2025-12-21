from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        # Sort the array in descending order
        # This allows us to easily access the two largest and smallest values
        sorted_nums = sorted(nums, reverse=True)

        # To maximize a + b - c:
        # - a and b should be the two largest values (maximize addition)
        # - c should be the smallest value (minimize subtraction, i.e., subtract the smallest)
        # Since we sorted in descending order:
        # - sorted_nums[0] is the largest
        # - sorted_nums[1] is the second largest
        # - sorted_nums[-1] is the smallest
        return sorted_nums[0] + sorted_nums[1] - sorted_nums[-1]
