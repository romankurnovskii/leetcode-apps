import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine profits and capital, sort by capital
        projects = list(zip(capital, profits))
        projects.sort()
        
        max_heap = []
        i = 0
        res = w
        
        for _ in range(k):
            # Add all projects we can afford to the heap
            while i < len(projects) and projects[i][0] <= res:
                heapq.heappush(max_heap, -projects[i][1])  # Negative for max heap
                i += 1
            
            if not max_heap:
                break
            
            # Take the project with maximum profit
            res += -heapq.heappop(max_heap)
        
        return res

