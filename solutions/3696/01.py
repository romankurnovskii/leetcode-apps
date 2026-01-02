from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                if words[i] != words[j]:
                    res = max(res, j - i)

        return res
