from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Floyd-Warshall algorithm
        INF = float("inf")
        dist = [[INF] * n for _ in range(n)]

        # Initialize distances
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Find city with minimum reachable cities
        min_count = n
        res = 0

        for i in range(n):
            count = sum(
                1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold
            )
            if count <= min_count:
                min_count = count
                res = i

        return res
