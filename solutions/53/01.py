from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            # If current sum becomes negative, reset it
            if current_sum < 0:
                current_sum = 0
            # Add current number
            current_sum += num
            # Update maximum sum
            max_sum = max(max_sum, current_sum)

        return max_sum
