class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        
        n = len(points)
        if n == 1:
            return 0
        
        # Prim's algorithm using min heap
        # Start with point 0
        visited = set()
        heap = [(0, 0)]  # (cost, point_index)
        res = 0
        
        while len(visited) < n:
            cost, curr = heapq.heappop(heap)
            
            if curr in visited:
                continue
            
            visited.add(curr)
            res += cost
            
            # Add all unvisited neighbors to heap
            for i in range(n):
                if i not in visited:
                    # Calculate Manhattan distance
                    dist = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    heapq.heappush(heap, (dist, i))
        
        return res

