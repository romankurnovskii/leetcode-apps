class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Simple string matching
        n = len(haystack)
        m = len(needle)

        # Check each possible starting position
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i

        # Not found
        return -1
