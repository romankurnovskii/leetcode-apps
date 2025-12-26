class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        n = len(edges) + 1
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))

        res = [0] * n

        # For each node as root, count pairs
        for root in range(n):

            def dfs(node, parent, dist):
                # Count if current distance is divisible by signalSpeed (and not root)
                cnt = 1 if dist > 0 and dist % signalSpeed == 0 else 0
                pairs = 0

                for neighbor, weight in graph[node]:
                    if neighbor != parent:
                        subtree_cnt = dfs(neighbor, node, dist + weight)
                        # Count pairs: current count * subtree count
                        pairs += cnt * subtree_cnt
                        cnt += subtree_cnt

                # If at root, return pairs; otherwise return count
                return pairs if node == root else cnt

            res[root] = dfs(root, root, 0)

        return res
