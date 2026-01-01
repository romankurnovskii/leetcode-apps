class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        res = 0

        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            res += 1

        return res
