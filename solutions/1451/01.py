from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        from collections import defaultdict

        # Build graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Tarjan's algorithm
        disc = [-1] * n  # Discovery time
        low = [-1] * n  # Lowest discovery time reachable
        time = 0
        res = []

        def dfs(u, parent):
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue

                if disc[v] == -1:  # Not visited
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # If low[v] > disc[u], then (u, v) is a bridge
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return res
