from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        # Calculate the average
        average = sum(nums) / len(nums)

        # Convert nums to a set for O(1) lookup
        nums_set = set(nums)

        # Start from the smallest integer greater than the average
        # If average is 4.5, we want 5 (floor(4.5) + 1 = 5)
        # If average is 4.0, we want 5 (floor(4.0) + 1 = 5)
        res = int(average) + 1

        # If average is negative or zero, we need to start from 1 (smallest positive)
        if res < 1:
            res = 1

        # Increment res until we find a positive integer that is not in the array
        while res in nums_set:
            res += 1

        return res
