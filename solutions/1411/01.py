class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # Two types of rows: ABA and ABC
        aba = 6  # 3 colors * 2 patterns
        abc = 6  # 3 colors * 2 patterns

        for i in range(1, n):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD
            aba, abc = new_aba, new_abc

        res = (aba + abc) % MOD
        return res
