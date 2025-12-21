class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate distance squared (no need for sqrt)
        def distance_sq(point):
            return point[0] ** 2 + point[1] ** 2

        # Sort by distance
        points.sort(key=distance_sq)

        return points[:k]
