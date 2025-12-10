from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7

        n = len(complexity)

        # Check if complexity[0] is the unique minimum
        min_complexity = complexity[0]
        min_count = sum(1 for c in complexity if c == min_complexity)

        if min_count > 1:
            # If there are other elements with the same complexity as index 0, no valid permutations
            return 0

        # Index 0 must be first. The remaining n-1 indices can be arranged in any order
        # So the answer is (n-1)!
        res = 1
        for i in range(1, n):
            res = (res * i) % MOD

        return res

