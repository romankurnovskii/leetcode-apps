class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid is greater than its right neighbor, peak is in left half
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                # Otherwise, peak is in right half
                left = mid + 1
        
        return left

