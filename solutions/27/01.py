from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize slow pointer
        slow = 0

        # Iterate through the array with fast pointer
        for fast in range(len(nums)):
            # If current element is not equal to val, keep it
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        # Return the count of elements not equal to val
        return slow
