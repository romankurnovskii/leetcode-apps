class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        res = 0
        
        for i in range(len(points)):
            slope_count = {}
            same_point = 1
            
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Same point
                if x1 == x2 and y1 == y2:
                    same_point += 1
                    continue
                
                # Calculate slope
                dx = x2 - x1
                dy = y2 - y1
                
                # Reduce to simplest form using GCD
                g = self.gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g
                
                slope = (dx, dy)
                slope_count[slope] = slope_count.get(slope, 0) + 1
            
            # Find max points on same line
            max_points = same_point
            if slope_count:
                max_points += max(slope_count.values())
            
            res = max(res, max_points)
        
        return res
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

