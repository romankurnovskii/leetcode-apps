from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        from collections import defaultdict

        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            total_time = 0

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                child_time = dfs(neighbor, node)

                # If child has apples or child subtree has apples, we need to visit it
                if child_time > 0 or hasApple[neighbor]:
                    total_time += child_time + 2  # 2 seconds: go and come back

            return total_time

        res = dfs(0, -1)
        return res
