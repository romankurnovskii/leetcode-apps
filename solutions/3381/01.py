from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Calculate prefix sums: prefix[i] = sum of nums[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Track minimum prefix sum for each residue class (index % k)
        # min_prefix[r] = minimum prefix sum at position i where i % k == r
        # Initialize with prefix[0] = 0 for residue 0
        min_prefix = {0: prefix[0]}
        
        res = float('-inf')
        
        # For each position i (1 to n), check valid subarrays ending at i-1
        for i in range(1, n + 1):
            r = i % k  # residue class
            
            # First, check if we can form a valid subarray using previous minimum
            if r in min_prefix:
                # Calculate sum: prefix[i] - min_prefix[r]
                # This gives sum of subarray from min_prefix position to i-1
                # Length = (i-1) - (min_prefix position) + 1
                # Since both i and min_prefix position have same residue r,
                # their difference is divisible by k
                current_sum = prefix[i] - min_prefix[r]
                res = max(res, current_sum)
            
            # Then update minimum prefix sum for this residue class
            if r not in min_prefix:
                min_prefix[r] = prefix[i]
            else:
                min_prefix[r] = min(min_prefix[r], prefix[i])
        
        return res
