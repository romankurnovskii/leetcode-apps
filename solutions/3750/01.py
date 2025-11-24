class Solution:
    def minimumFlips(self, n: int) -> int:
        # Convert n to binary string, slicing off the "0b" prefix
        s = bin(n)[2:]

        res = 0
        l = 0
        r = len(s) - 1

        # Use two pointers to compare symmetric bits
        while l < r:
            # If the bits at the symmetric positions are different
            # we need to flip both to make the number equal to its reverse.
            if s[l] != s[r]:
                res += 2

            l += 1
            r -= 1

        return res
