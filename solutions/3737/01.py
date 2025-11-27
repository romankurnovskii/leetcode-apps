from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        
        # Check all possible subarrays
        for i in range(n):
            count = 0  # Count of target in current subarray
            for j in range(i, n):
                # Add current element to subarray
                if nums[j] == target:
                    count += 1
                
                # Check if target is majority: 2 * count > length
                length = j - i + 1
                if 2 * count > length:
                    res += 1
        
        return res

