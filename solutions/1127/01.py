from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use max heap (negate values since Python has min heap)
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            # Get two largest stones
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            # If they're different, add the difference back
            if first != second:
                heapq.heappush(heap, -(first - second))
        
        # Return the last stone weight, or 0 if no stones left
        return -heap[0] if heap else 0

