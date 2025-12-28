class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Check if graph is connected using DFS
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  # Cycle detected
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent:  # Skip the parent to avoid false cycle detection
                    if not dfs(neighbor, node):
                        return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Check if all nodes are visited (graph is connected)
        return len(visited) == n
