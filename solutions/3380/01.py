class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        res = -1

        # Try all combinations of 4 points
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Check if they can form opposite corners (must have different x and y)
                if x1 != x2 and y1 != y2:
                    # The other two corners would be (x1, y2) and (x2, y1)
                    corner3 = [x1, y2]
                    corner4 = [x2, y1]

                    # Check if corner3 and corner4 exist in points
                    if corner3 in points and corner4 in points:
                        # Check if rectangle doesn't contain other points
                        min_x, max_x = min(x1, x2), max(x1, x2)
                        min_y, max_y = min(y1, y2), max(y1, y2)

                        valid = True
                        corners = {
                            tuple(points[i]),
                            tuple(points[j]),
                            tuple(corner3),
                            tuple(corner4),
                        }
                        for point in points:
                            px, py = point
                            point_tuple = tuple(point)
                            # Skip if it's one of the corners
                            if point_tuple in corners:
                                continue
                            # Check if point is inside or on border
                            if min_x <= px <= max_x and min_y <= py <= max_y:
                                valid = False
                                break

                        if valid:
                            area = abs(x2 - x1) * abs(y2 - y1)
                            res = max(res, area)

        return res
