from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handle edge cases
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        # Initialize slow pointer
        slow = 1

        # Iterate through the array with fast pointer
        for fast in range(1, len(nums)):
            # If current element is different from previous, it's unique
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        # Return the count of unique elements
        return slow
