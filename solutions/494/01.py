from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Use memoization to avoid recalculating
        memo = {}
        
        def dfs(index, current_sum):
            # Base case: if we've processed all numbers
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Check memoization
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Try both adding and subtracting current number
            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])
            
            # Store result in memo
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]
        
        return dfs(0, 0)

