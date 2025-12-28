class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        i, j, k = 0, 1, 0

        # Use two pointers to find the lexicographically largest suffix
        while j + k < n:
            if s[i + k] == s[j + k]:
                # Characters match, continue comparing
                k += 1
            elif s[i + k] < s[j + k]:
                # s[j:] is larger, update i to skip smaller prefixes
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            else:
                # s[i:] is larger, skip j and continue
                j = j + k + 1
                k = 0

        return s[i:]
