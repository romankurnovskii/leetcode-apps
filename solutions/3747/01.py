class Solution:
    def countDistinct(self, n: int) -> int:
        # Convert n to string for digit manipulation
        s = str(n)
        length = len(s)
        
        # Precompute powers of 9 (for digits 1-9, excluding 0)
        pow9 = [1] * (length + 1)
        for i in range(1, length + 1):
            pow9[i] = pow9[i - 1] * 9
        
        res = 0
        
        # Count all numbers with fewer digits than n
        # For each length l from 1 to length-1, there are 9^l numbers without zeros
        for l in range(1, length):
            res += pow9[l]
        
        # Count numbers with same number of digits as n but <= n
        for i in range(length):
            digit = int(s[i])
            
            # If we encounter a zero, we can't form any more valid numbers
            if digit == 0:
                return res
            
            # For each digit d from 1 to digit-1, we can form
            # pow9[remaining_positions] numbers
            for d in range(1, digit):
                res += pow9[length - i - 1]
        
        # Add 1 if n itself has no zeros
        return res + 1

