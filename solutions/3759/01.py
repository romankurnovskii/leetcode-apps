class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Build graph: character -> character with cost
        # Use Floyd-Warshall to find shortest path between all pairs
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        
        # Initialize: same character costs 0
        for i in range(26):
            dist[i][i] = 0
        
        # Add edges from original to changed
        for i in range(len(original)):
            orig_char = ord(original[i]) - ord('a')
            changed_char = ord(changed[i]) - ord('a')
            cost_val = cost[i]
            # Keep minimum cost if multiple edges exist
            dist[orig_char][changed_char] = min(dist[orig_char][changed_char], cost_val)
        
        # Floyd-Warshall algorithm
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate total cost
        res = 0
        for i in range(len(source)):
            src_char = ord(source[i]) - ord('a')
            tgt_char = ord(target[i]) - ord('a')
            
            if src_char == tgt_char:
                continue
            
            if dist[src_char][tgt_char] == INF:
                return -1
            
            res += dist[src_char][tgt_char]
        
        return res
