class Solution:
    def mirrorDistance(self, num: int) -> int:
        s = str(num)
        n = len(s)
        res = 0

        for i in range(n // 2):
            left = int(s[i])
            right = int(s[n - 1 - i])
            res += abs(left - right)

        return res
