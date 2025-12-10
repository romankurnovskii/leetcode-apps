class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        # All computers i > 0 must have complexity[i] > complexity[0]
        # If any computer has complexity <= complexity[0], it can never be unlocked
        res = 1
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
            res = (res * i) % MOD

        return res
