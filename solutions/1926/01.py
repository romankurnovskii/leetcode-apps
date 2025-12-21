from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque([(entrance[0], entrance[1], 0)])
        visited = {(entrance[0], entrance[1])}

        while queue:
            row, col, steps = queue.popleft()

            # Check if we're at an exit (boundary and not entrance)
            if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                if [row, col] != entrance:
                    return steps

            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and maze[new_row][new_col] == "."
                    and (new_row, new_col) not in visited
                ):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))

        return -1
