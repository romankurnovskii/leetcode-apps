class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq
        
        heapq.heapify(sticks)
        res = 0
        
        while len(sticks) > 1:
            # Get two shortest sticks
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            
            # Cost is sum of two sticks
            cost = first + second
            res += cost
            
            # Add merged stick back
            heapq.heappush(sticks, cost)
        
        return res

