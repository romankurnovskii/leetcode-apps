from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Track the maximum position we can reach
        max_reach = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If we can't reach the current position, we can't reach the end
            if i > max_reach:
                return False

            # Update the maximum position we can reach
            max_reach = max(max_reach, i + nums[i])

        # If we can reach the last position, return true
        return True
