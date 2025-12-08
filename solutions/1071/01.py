class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 == str2 + str1
        # This is necessary for a common divisor to exist
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find GCD of lengths using Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # The GCD string will have length equal to GCD of the two string lengths
        gcd_len = gcd(len(str1), len(str2))
        
        # Return the prefix of length gcd_len
        return str1[:gcd_len]
