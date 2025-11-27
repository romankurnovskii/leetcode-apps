from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        left = 0
        right = len(nums) - 1
        
        # Binary search
        while left <= right:
            # Calculate middle index
            mid = (left + right) // 2
            
            # If target found at mid
            if nums[mid] == target:
                return mid
            
            # If target is smaller, search left half
            elif nums[mid] > target:
                right = mid - 1
            
            # If target is larger, search right half
            else:
                left = mid + 1
        
        # Target not found
        return -1


