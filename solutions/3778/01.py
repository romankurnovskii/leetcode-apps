from typing import List


class Solution:
    def minDistance(self, edges: List[List[int]], n: int) -> int:
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def dijkstra(exclude_edge):
            dist = [float("inf")] * (n + 1)
            dist[1] = 0
            pq = [(0, 1)]

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue

                for v, w in graph[u]:
                    if (u, v) == exclude_edge or (v, u) == exclude_edge:
                        continue
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))

            return dist[n]

        max_edge = None
        max_weight = -1

        for u, v, w in edges:
            if w > max_weight:
                max_weight = w
                max_edge = (u, v)

        res = dijkstra(max_edge)
        return res if res != float("inf") else -1
