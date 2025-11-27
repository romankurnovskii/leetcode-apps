class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        j = 0  # pointer for t
        
        # Traverse both strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # move pointer in s
            j += 1  # always move pointer in t
        
        # If we've matched all characters in s, it's a subsequence
        return i == len(s)
