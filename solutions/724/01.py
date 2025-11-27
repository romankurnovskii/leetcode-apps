from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate total sum of the array
        total_sum = sum(nums)
        
        # Track left sum as we iterate
        left_sum = 0
        
        # For each index, check if left_sum equals right_sum
        # right_sum = total_sum - left_sum - nums[i]
        # So we need: left_sum == total_sum - left_sum - nums[i]
        # Which simplifies to: 2 * left_sum == total_sum - nums[i]
        for i in range(len(nums)):
            # Check if current index is pivot
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            # Update left_sum for next iteration
            left_sum += nums[i]
        
        return -1

