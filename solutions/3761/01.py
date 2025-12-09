class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(n):
            # Reverse digits, removing leading zeros
            return int(str(n)[::-1])
        
        # Map: reversed value -> most recent index
        seen = {}
        res = float('inf')
        
        for i, num in enumerate(nums):
            reversed_val = reverse_num(num)
            
            # Check if current number matches any reversed value we've seen
            if num in seen:
                res = min(res, i - seen[num])
            
            # Store current index under the reversed value
            seen[reversed_val] = i
        
        return res if res != float('inf') else -1
