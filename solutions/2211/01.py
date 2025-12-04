class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove leading L's (moving left, will never collide)
        # Remove trailing R's (moving right, will never collide)
        # Only cars in the middle section will collide
        directions = directions.lstrip('L').rstrip('R')
        
        if not directions:
            return 0
        
        res = 0
        # Count all non-stationary cars in the middle section
        # Each R or L in the middle will eventually collide
        for char in directions:
            if char != 'S':
                res += 1
        
        return res

