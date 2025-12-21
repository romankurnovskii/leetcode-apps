from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            # Number of 1s in i is same as i//2, plus 1 if i is odd
            res[i] = res[i // 2] + (i % 2)

        return res
