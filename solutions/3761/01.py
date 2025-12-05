class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # Sieve of Eratosthenes to find primes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Build tree
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # DP: dp[node][0] = paths with 0 primes, dp[node][1] = paths with 1 prime
        dp = [[0, 0] for _ in range(n + 1)]
        res = 0
        
        def dfs(node, parent):
            nonlocal res
            
            if is_prime[node]:
                dp[node][1] = 1
            else:
                dp[node][0] = 1
            
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    # Count paths passing through current node
                    # Path with 1 prime: (node has 1 prime, child has 0) or (node has 0, child has 1)
                    res += dp[node][1] * dp[child][0] + dp[node][0] * dp[child][1]
                    
                    # Update dp for current node
                    if is_prime[node]:
                        dp[node][1] += dp[child][0]
                    else:
                        dp[node][0] += dp[child][0]
                        dp[node][1] += dp[child][1]
        
        dfs(1, 0)
        return res
