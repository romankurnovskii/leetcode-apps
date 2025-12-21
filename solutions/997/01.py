from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Count how many people trust each person
        trust_count = [0] * (n + 1)
        # Count how many people each person trusts
        trusting_count = [0] * (n + 1)

        for a, b in trust:
            trusting_count[a] += 1  # person a trusts someone
            trust_count[b] += 1  # person b is trusted by someone

        # The judge trusts nobody (trusting_count[i] == 0)
        # and is trusted by everyone else (trust_count[i] == n - 1)
        for i in range(1, n + 1):
            if trusting_count[i] == 0 and trust_count[i] == n - 1:
                return i

        return -1
