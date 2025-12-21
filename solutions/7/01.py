class Solution:
    def reverse(self, x: int) -> int:
        # Handle negative numbers
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # Apply sign and check for overflow
        result = sign * reversed_num

        # Check 32-bit integer bounds
        if result < -(2**31) or result > 2**31 - 1:
            return 0

        return result
