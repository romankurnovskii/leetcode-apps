import functools


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # Build hat-to-people mapping
        htop = [[] for _ in range(41)]  # htop: hat to people list
        for p, prefer_hats in enumerate(hats):
            for h in prefer_hats:
                htop[h].append(p)

        # Filter out hats no one wants
        htop = list(filter(lambda h: h, htop))

        num_hats, num_people = len(htop), len(hats)
        if num_hats < num_people:
            return 0

        MOD = 10**9 + 7

        @functools.lru_cache(None)
        def dp(i, mask):
            # If all people have hats assigned
            if bin(mask).count("1") == num_people:
                return 1
            # If we've processed all hats
            if i == num_hats:
                return 0

            # Don't use current hat
            res = dp(i + 1, mask)

            # Try assigning current hat to each person who wants it
            for p in htop[i]:
                if mask & (1 << p) == 0:  # Person p doesn't have a hat yet
                    mask |= 1 << p
                    res += dp(i + 1, mask)
                    mask ^= 1 << p

            return res % MOD

        res = dp(0, 0)
        return res
