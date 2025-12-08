class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        res = -1

        # Try all combinations of 4 points
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # Check if they can form opposite corners
                # The other two corners would be (x1, y2) and (x2, y1)
                corner3 = [x1, y2]
                corner4 = [x2, y1]

                # Check if corner3 and corner4 exist in points
                if corner3 in points and corner4 in points:
                    # Check if rectangle doesn't contain other points
                    min_x, max_x = min(x1, x2), max(x1, x2)
                    min_y, max_y = min(y1, y2), max(y1, y2)

                    valid = True
                    for point in points:
                        px, py = point
                        # Check if point is inside or on border (but not a corner)
                        if (
                            (min_x < px < max_x and min_y < py < max_y)
                            or (
                                min_x < px < max_x
                                and min_y <= py <= max_y
                                and point
                                not in [points[i], points[j], corner3, corner4]
                            )
                            or (
                                min_x <= px <= max_x
                                and min_y < py < max_y
                                and point
                                not in [points[i], points[j], corner3, corner4]
                            )
                        ):
                            valid = False
                            break

                    if valid:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        res = max(res, area)

        return res
