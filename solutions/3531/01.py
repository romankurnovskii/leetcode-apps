from typing import List
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Group buildings by x and y coordinates
        by_x = defaultdict(list)
        by_y = defaultdict(list)

        for x, y in buildings:
            by_x[x].append(y)
            by_y[y].append(x)

        # Sort each group
        for x in by_x:
            by_x[x].sort()
        for y in by_y:
            by_y[y].sort()

        res = 0

        # Check each building
        for x, y in buildings:
            # Check if it has buildings in all four directions
            # Check above (same x, smaller y) - use binary search
            has_above = False
            if x in by_x:
                y_list = by_x[x]
                # Check if there's any y < current y
                if y_list and y_list[0] < y:
                    has_above = True

            # Check below (same x, larger y)
            has_below = False
            if x in by_x:
                y_list = by_x[x]
                # Check if there's any y > current y
                if y_list and y_list[-1] > y:
                    has_below = True

            # Check left (same y, smaller x)
            has_left = False
            if y in by_y:
                x_list = by_y[y]
                # Check if there's any x < current x
                if x_list and x_list[0] < x:
                    has_left = True

            # Check right (same y, larger x)
            has_right = False
            if y in by_y:
                x_list = by_y[y]
                # Check if there's any x > current x
                if x_list and x_list[-1] > x:
                    has_right = True

            if has_above and has_below and has_left and has_right:
                res += 1

        return res
