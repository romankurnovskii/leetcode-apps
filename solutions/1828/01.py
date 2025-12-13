from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for query in queries:
            x, y, r = query
            count = 0
            
            # Check each point
            for point in points:
                px, py = point
                # Calculate distance from point to circle center
                distance_squared = (px - x) ** 2 + (py - y) ** 2
                
                # Point is inside if distance <= radius
                if distance_squared <= r * r:
                    count += 1
            
            res.append(count)
        
        return res

