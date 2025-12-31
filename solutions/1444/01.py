from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])

        # Precompute prefix sum for apples
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                prefix[i][j] = (
                    (1 if pizza[i][j] == "A" else 0)
                    + prefix[i + 1][j]
                    + prefix[i][j + 1]
                    - prefix[i + 1][j + 1]
                )

        # Memoization
        from functools import lru_cache

        @lru_cache(None)
        def dp(r, c, cuts_left):
            # Check if current piece has at least one apple
            if prefix[r][c] == 0:
                return 0

            if cuts_left == 0:
                return 1

            res = 0

            # Try horizontal cuts
            for i in range(r + 1, rows):
                if prefix[r][c] - prefix[i][c] > 0:  # Top piece has apple
                    res = (res + dp(i, c, cuts_left - 1)) % MOD

            # Try vertical cuts
            for j in range(c + 1, cols):
                if prefix[r][c] - prefix[r][j] > 0:  # Left piece has apple
                    res = (res + dp(r, j, cuts_left - 1)) % MOD

            return res

        res = dp(0, 0, k - 1)
        return res
