class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        res = 0

        def dfs(node, parent):
            nonlocal res
            for neighbor, direction in graph[node]:
                if neighbor == parent:
                    continue
                if direction == 1:
                    res += 1
                dfs(neighbor, node)

        dfs(0, -1)
        return res
