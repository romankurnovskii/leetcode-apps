from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Calculate total sum of the array
        total_sum = sum(nums)
        
        # Track left sum as we iterate
        left_sum = 0
        
        # Iterate through each index
        for i in range(len(nums)):
            # Right sum = total sum - left sum - current element
            right_sum = total_sum - left_sum - nums[i]
            
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i
            
            # Add current element to left sum for next iteration
            left_sum += nums[i]
        
        # No pivot index found
        return -1


