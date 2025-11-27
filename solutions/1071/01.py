class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if strings can be divided by each other
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find GCD of lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
