from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # Greedy approach: track farthest reachable position
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            # Update farthest reachable position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can reach the end, we're done
                if current_end >= n - 1:
                    break
        
        return jumps

