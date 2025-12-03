class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        # Base case
        if n == 0:
            return 1.0
        
        # Recursive approach: x^n = (x^(n/2))^2 if n is even
        #                    x^n = x * (x^(n/2))^2 if n is odd
        res = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return res * res
        else:
            return x * res * res

