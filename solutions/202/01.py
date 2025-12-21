class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            # Calculate sum of squares of digits
            res = 0
            while n > 0:
                digit = n % 10
                res += digit * digit
                n //= 10
            n = res

        return True
