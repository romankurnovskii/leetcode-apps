"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def build(r1, c1, r2, c2):
            # Check if all values in the grid are the same
            all_same = True
            first_val = grid[r1][c1]

            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break

            if all_same:
                return Node(first_val == 1, True, None, None, None, None)

            # Divide into four quadrants
            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2

            top_left = build(r1, c1, mid_r, mid_c)
            top_right = build(r1, mid_c + 1, mid_r, c2)
            bottom_left = build(mid_r + 1, c1, r2, mid_c)
            bottom_right = build(mid_r + 1, mid_c + 1, r2, c2)

            return Node(False, False, top_left, top_right, bottom_left, bottom_right)

        n = len(grid)
        res = build(0, 0, n - 1, n - 1)
        return res
