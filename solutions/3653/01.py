class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # Sieve of Eratosthenes to find primes
        prime = [True] * (n + 1)
        prime[1] = False

        all_primes = []
        for i in range(2, n + 1):
            if prime[i]:
                all_primes.append(i)
            for x in all_primes:
                temp = i * x
                if temp > n:
                    break
                prime[temp] = False
                if i % x == 0:
                    break

        # Build graph
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0]

        def mul(x, y):
            return x * y

        def dfs(x, parent, graph, prime, res):
            # v[0] = paths with no primes, v[1] = paths with one prime
            v = [1 - prime[x], prime[x]]

            for y in graph[x]:
                if y == parent:
                    continue
                p = dfs(y, x, graph, prime, res)
                # Count paths passing through x with exactly one prime
                res[0] += mul(p[0], v[1]) + mul(p[1], v[0])

                if prime[x]:
                    v[1] += p[0]
                else:
                    v[0] += p[0]
                    v[1] += p[1]

            return v

        dfs(1, 0, graph, prime, res)
        return res[0]
