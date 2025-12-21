from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Two pointers: one for current position, one for next non-zero position
        next_non_zero = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                next_non_zero += 1
