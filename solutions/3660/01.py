class Solution:
    def minimumTotalPrice(
        self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]
    ) -> int:
        from collections import defaultdict, Counter

        # Build graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Count how many times each node is visited
        count = Counter()
        total_cost = 0

        # DFS to find path from start to end
        def dfs_path(node, parent, end):
            nonlocal count, total_cost
            if node == end:
                return True

            for neighbor in graph[node]:
                if neighbor != parent:
                    if dfs_path(neighbor, node, end):
                        count[neighbor] += 1
                        total_cost += price[neighbor]
                        return True
            return False

        # Process all trips
        for start, end in trips:
            count[start] += 1
            total_cost += price[start]
            dfs_path(start, None, end)

        # DP to find maximum reduction
        from functools import lru_cache

        @lru_cache(None)
        def dp(node, parent, can_reduce):
            if can_reduce:
                res = (price[node] // 2) * count[node]
            else:
                res = 0

            reduction = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    if can_reduce:
                        # If current node is reduced, neighbor cannot be reduced
                        cur = dp(neighbor, node, False)
                    else:
                        # If current node is not reduced, neighbor can be reduced or not
                        cur = max(dp(neighbor, node, False), dp(neighbor, node, True))
                    reduction += cur

            return res + reduction

        # Find maximum reduction starting from any node
        max_reduction = 0
        for i in range(n):
            max_reduction = max(max_reduction, dp(i, None, True), dp(i, None, False))

        return total_cost - max_reduction
