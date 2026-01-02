from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        total_ones = s.count("1")
        res = 0
        left_zeros = 0
        left_ones = 0

        for i in range(n - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                left_ones += 1

            right_ones = total_ones - left_ones
            res = max(res, left_zeros + right_ones)

        return res
