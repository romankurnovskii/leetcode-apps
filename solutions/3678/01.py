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
        x = int(average) + 1
        
        # If average is negative or zero, we need to start from 1 (smallest positive)
        if x < 1:
            x = 1
        
        # Increment x until we find a positive integer that is not in the array
        while x in nums_set:
            x += 1
        
        return x

