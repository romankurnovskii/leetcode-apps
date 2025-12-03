class Solution:
    def reverse(self, x: int) -> int:
        """Reverse the digits of an integer, removing leading zeros."""
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res
    
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Map to store last occurrence index of reversed numbers
        last_occ = {}
        
        # Store reverse of first element
        last_occ[self.reverse(nums[0])] = 0
        
        res = float('inf')
        
        # Process from index 1 onwards
        for j in range(1, len(nums)):
            # If current number appeared as a reversed number before
            if nums[j] in last_occ:
                res = min(res, j - last_occ[nums[j]])
            
            # Update last occurrence of reversed current number
            last_occ[self.reverse(nums[j])] = j
        
        return res if res != float('inf') else -1

