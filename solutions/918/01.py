from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Case 1: Maximum subarray is in the middle (normal case)
        max_sum = nums[0]
        current_max = 0

        # Case 2: Maximum subarray wraps around (circular)
        # This means we want to minimize the middle part
        min_sum = nums[0]
        current_min = 0
        total_sum = 0

        for num in nums:
            # Normal maximum subarray
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            # Minimum subarray (for circular case)
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)

            total_sum += num

        # If all numbers are negative, return max_sum
        if max_sum < 0:
            return max_sum

        # Return max of normal case and circular case
        return max(max_sum, total_sum - min_sum)
