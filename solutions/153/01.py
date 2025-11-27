from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If right half is sorted, minimum is in left half
            if nums[mid] < nums[right]:
                right = mid
            # Otherwise, minimum is in right half
            else:
                left = mid + 1
        
        return nums[left]

