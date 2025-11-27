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
        
        # Apply sign
        reversed_num *= sign
        
        # Check for 32-bit integer overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

