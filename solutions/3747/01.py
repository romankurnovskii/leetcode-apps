class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        length = len(s)

        pow9 = [1] * (length + 1)
        for i in range(1, length + 1):
            pow9[i] = pow9[i - 1] * 9

        res = 0
        # Count zero-free numbers with fewer digits
        for d in range(1, length):
            res += pow9[d]

        # Count zero-free numbers with same length as n
        for i, ch in enumerate(s):
            digit = int(ch)
            if digit == 0:
                return res
            res += (digit - 1) * pow9[length - i - 1]

        # n itself is zero-free
        return res + 1
