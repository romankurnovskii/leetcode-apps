from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Find all rotten oranges and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh_count += 1

        # If no fresh oranges, return 0
        if fresh_count == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_time = 0

        # BFS to rot oranges
        while queue:
            r, c, time = queue.popleft()
            max_time = max(max_time, time)

            # Check all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check bounds and if orange is fresh
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    # Rot the orange
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc, time + 1))

        # If there are still fresh oranges, return -1
        return max_time if fresh_count == 0 else -1
