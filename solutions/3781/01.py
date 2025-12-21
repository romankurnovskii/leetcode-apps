class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        import heapq
        
        # Use max heap (negate values for Python's min heap)
        heap = []
        res = 0
        
        for i in range(len(nums)):
            # Add current number to heap (negate for max heap)
            heapq.heappush(heap, -nums[i])
            
            # If s[i] == '1', we must select a number
            if s[i] == '1':
                # Get the maximum value from heap
                max_val = -heapq.heappop(heap)
                res += max_val
        
        return res

