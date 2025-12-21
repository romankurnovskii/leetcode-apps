class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Process from right to left using a copy
        nums = nums[:]  # Work with a copy to avoid modifying input
        seen = {nums.pop()}
        
        while nums:
            if nums[-1] in seen:
                # Calculate operations needed: (remaining + 2) // 3
                return (len(nums) + 2) // 3
            seen.add(nums.pop())
        
        return 0

