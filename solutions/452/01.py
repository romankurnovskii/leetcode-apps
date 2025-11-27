from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort balloons by end coordinate
        points.sort(key=lambda x: x[1])
        
        # Count of arrows needed
        res = 0
        
        # Track the position of the last arrow
        last_arrow = float('-inf')
        
        # Iterate through sorted balloons
        for start, end in points:
            # If current balloon is not burst by last arrow
            if start > last_arrow:
                # Need a new arrow at the end of this balloon
                res += 1
                last_arrow = end
        
        return res


