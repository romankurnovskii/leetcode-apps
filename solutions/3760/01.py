class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Assign unique IDs to all unique strings
        string_to_id = {}
        id_counter = 0
        
        all_strings = set(original) | set(changed)
        for s in all_strings:
            if s not in string_to_id:
                string_to_id[s] = id_counter
                id_counter += 1
        
        n_strings = len(string_to_id)
        INF = float('inf')
        
        # Build graph with Floyd-Warshall
        dist = [[INF] * n_strings for _ in range(n_strings)]
        
        # Initialize: same string costs 0
        for i in range(n_strings):
            dist[i][i] = 0
        
        # Add edges
        for i in range(len(original)):
            orig_id = string_to_id[original[i]]
            changed_id = string_to_id[changed[i]]
            cost_val = cost[i]
            dist[orig_id][changed_id] = min(dist[orig_id][changed_id], cost_val)
        
        # Floyd-Warshall
        for k in range(n_strings):
            for i in range(n_strings):
                for j in range(n_strings):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # DP: dp[i] = minimum cost to convert first i characters
        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            # Option 1: No change if characters match
            if source[i-1] == target[i-1]:
                dp[i] = min(dp[i], dp[i-1])
            
            # Option 2: Try all possible substring conversions ending at i
            for j in range(i):
                substr_src = source[j:i]
                substr_tgt = target[j:i]
                
                if substr_src in string_to_id and substr_tgt in string_to_id:
                    src_id = string_to_id[substr_src]
                    tgt_id = string_to_id[substr_tgt]
                    
                    if dist[src_id][tgt_id] != INF:
                        dp[i] = min(dp[i], dp[j] + dist[src_id][tgt_id])
        
        return dp[n] if dp[n] != INF else -1
