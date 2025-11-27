class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand_around_center(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right are now one step beyond the palindrome
            length = right - left - 1
            if length > max_len:
                max_len = length
                start = left + 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes
            expand_around_center(i, i)
            # Check for even-length palindromes
            expand_around_center(i, i + 1)
        
        return s[start:start + max_len]

