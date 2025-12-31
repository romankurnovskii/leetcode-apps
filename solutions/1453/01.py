from typing import List
from collections import deque


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        # 0-1 BFS: weight 0 for following direction, weight 1 for changing
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0
        dq = deque([(0, 0)])

        while dq:
            r, c = dq.popleft()

            if r == rows - 1 and c == cols - 1:
                return dist[r][c]

            for dir_num, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = 0 if grid[r][c] == dir_num else 1
                    new_dist = dist[r][c] + cost

                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return dist[rows - 1][cols - 1]
