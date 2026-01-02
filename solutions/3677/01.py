class Solution:
    def countPalindromicNumbers(self, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        res = 0

        for i in range(1, n + 1):
            binary = bin(i)[2:]
            if is_palindrome(binary):
                res += 1

        return res
