from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            # Expand window
            if nums[right] == 0:
                zero_count += 1

            # Shrink window if we have more than one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update maximum length (subtract 1 because we must delete one element)
            max_length = max(max_length, right - left)

        return max_length
