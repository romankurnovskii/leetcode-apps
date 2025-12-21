class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        # Find all divisors of n
        divisors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        divisors.sort()

        res = None
        min_diff = float("inf")

        def dfs(start, picked, prod, path):
            nonlocal res, min_diff

            if picked == k:
                if prod == n:
                    diff = max(path) - min(path)
                    if diff < min_diff:
                        min_diff = diff
                        res = path[:]
                return

            if prod > n:
                return

            for i in range(start, len(divisors)):
                divisor = divisors[i]
                if prod * divisor > n:
                    break
                path.append(divisor)
                dfs(i, picked + 1, prod * divisor, path)
                path.pop()

        dfs(0, 0, 1, [])
        return res
