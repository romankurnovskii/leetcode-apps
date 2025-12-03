from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        res = 0
        
        # Process all pairs of points
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                
                # Calculate slope and intercept
                if x2 == x1:
                    # Vertical line: infinite slope, use x-coordinate as intercept
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx
                
                # Store midpoint as single integer: (x1+x2)*10000 + (y1+y2)
                mid = (x1 + x2) * 10000 + (y1 + y2)
                
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)
        
        # Count trapezoids: for each slope, count pairs of segments with same slope
        for intercepts in slope_to_intercept.values():
            if len(intercepts) == 1:
                continue
            
            cnt = defaultdict(int)
            for b_val in intercepts:
                cnt[b_val] += 1
            
            # Count pairs: for each intercept count, multiply with previous total
            total_sum = 0
            for count in cnt.values():
                res += total_sum * count
                total_sum += count
        
        # Subtract parallelograms: segments with same midpoint but different slopes
        for slopes in mid_to_slope.values():
            if len(slopes) == 1:
                continue
            
            cnt = defaultdict(int)
            for k_val in slopes:
                cnt[k_val] += 1
            
            # Subtract pairs of different slopes at same midpoint
            total_sum = 0
            for count in cnt.values():
                res -= total_sum * count
                total_sum += count
        
        return res

