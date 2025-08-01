from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize candidate and count
        candidate = nums[0]
        count = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                # If count becomes 0, change candidate
                if count == 0:
                    candidate = nums[i]
                    count = 1

        # Return the majority element
        return candidate
