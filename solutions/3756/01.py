from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        p_val = [0] * (n + 1)
        p_cnt = [0] * (n + 1)
        p_sum = [0] * (n + 1)

        for i, char in enumerate(s):
            d = int(char)
            if d == 0:
                p_val[i + 1] = p_val[i]
                p_cnt[i + 1] = p_cnt[i]
                p_sum[i + 1] = p_sum[i]
            else:
                p_val[i + 1] = (p_val[i] * 10 + d) % MOD
                p_cnt[i + 1] = p_cnt[i] + 1
                p_sum[i + 1] = p_sum[i] + d

        max_pow = p_cnt[n]
        pow10 = [1] * (max_pow + 1)
        for i in range(1, max_pow + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        res = []

        for l, r in queries:
            # Get count of non-zero digits in range
            cnt = p_cnt[r + 1] - p_cnt[l]

            if cnt == 0:
                res.append(0)
                continue

            d_sum = p_sum[r + 1] - p_sum[l]

            full = p_val[r + 1]
            prev = p_val[l]

            # Remove the prefix 'prev' from 'full'.
            # We shift 'prev' to the left by 'cnt' (the size of the current range)
            # so it aligns with the 'full' number before subtracting.
            val = (full - (prev * pow10[cnt])) % MOD

            res.append((val * d_sum) % MOD)

        return res
