class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Find the closest point on rectangle to circle center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Calculate distance from circle center to closest point
        distance_sq = (xCenter - closest_x) ** 2 + (yCenter - closest_y) ** 2

        return distance_sq <= radius * radius
