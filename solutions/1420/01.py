class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][l] = number of arrays of length i, max value j, with l comparisons
        # We can optimize space by only keeping previous state
        prev = [[0] * (k + 1) for _ in range(m + 1)]
        prev[0][0] = 1

        for i in range(1, n + 1):
            curr = [[0] * (k + 1) for _ in range(m + 1)]
            for max_val in range(m + 1):
                for comparisons in range(k + 1):
                    if prev[max_val][comparisons] == 0:
                        continue

                    # Add number <= max_val (no new comparison)
                    curr[max_val][comparisons] = (
                        curr[max_val][comparisons]
                        + prev[max_val][comparisons] * max_val
                    ) % MOD

                    # Add number > max_val (new comparison)
                    if comparisons < k:
                        for new_max in range(max_val + 1, m + 1):
                            curr[new_max][comparisons + 1] = (
                                curr[new_max][comparisons + 1]
                                + prev[max_val][comparisons]
                            ) % MOD

            prev = curr

        res = sum(prev[i][k] for i in range(1, m + 1)) % MOD
        return res
