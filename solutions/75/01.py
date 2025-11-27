from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Dutch National Flag algorithm
        left = 0  # Points to the end of 0s
        right = len(nums) - 1  # Points to the start of 2s
        i = 0  # Current pointer
        
        while i <= right:
            if nums[i] == 0:
                # Swap with left pointer
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                # Swap with right pointer
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                # Don't increment i, need to check swapped value
            else:
                # nums[i] == 1, just move forward
                i += 1

