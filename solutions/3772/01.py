class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        # Build tree
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Rerooting DP
        # dp[node] = max score of connected subgraph containing node
        # We use tree DP with rerooting
        
        # First, calculate for each node the best subtree score
        def dfs(node, parent):
            # Score contribution of this node
            node_score = 1 if good[node] else -1
            
            # Best score including this node and its children
            best = node_score
            for child in graph[node]:
                if child != parent:
                    child_score = dfs(child, node)
                    # Include child if it improves the score
                    if child_score > 0:
                        best += child_score
            return best
        
        # For each node as root, calculate max score
        res = []
        for root in range(n):
            score = dfs(root, -1)
            res.append(score)
        
        return res
