class Solution:
    def maxSubgraphScore(
        self, n: int, edges: List[List[int]], good: List[int]
    ) -> List[int]:
        # Build tree
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Rerooting DP - O(n) solution
        # down[node] = max score of subtree rooted at node
        down = [0] * n

        def dfs1(node, parent):
            node_score = 1 if good[node] else -1
            score = node_score

            for child in graph[node]:
                if child != parent:
                    child_score = dfs1(child, node)
                    if child_score > 0:
                        score += child_score

            down[node] = score
            return score

        dfs1(0, -1)

        # ans[node] = max score when node is root
        ans = [0] * n
        ans[0] = down[0]

        def dfs2(node, parent):
            if parent != -1:
                # Standard rerooting formula:
                # ans[child] = down[child] + max(0, ans[parent] - max(0, down[child]))
                # But we need to account for the fact that ans[parent] includes down[node]
                # So parent's contribution without node = ans[parent] - max(0, down[node])
                parent_contrib = ans[parent] - max(0, down[node])
                ans[node] = down[node] + max(0, parent_contrib)

            for child in graph[node]:
                if child != parent:
                    dfs2(child, node)

        dfs2(0, -1)
        return ans
