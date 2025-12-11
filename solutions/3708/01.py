from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        res = 2  # Minimum valid length is 2
        current_length = 2

        # Check from index 2 onwards
        for i in range(2, n):
            # Check if current element equals sum of previous two
            if nums[i] == nums[i - 1] + nums[i - 2]:
                current_length += 1
            else:
                res = max(res, current_length)
                current_length = 2  # Reset to minimum valid length

        res = max(res, current_length)
        return res
