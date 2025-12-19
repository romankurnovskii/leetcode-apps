class Solution:
    def minOperations(self, s: str) -> int:
        # Find the character that takes the longest to become 'a'
        # Distance from 'a' in circular alphabet: (ord('a') + 26 - ord(c)) % 26
        res = 0
        for c in s:
            res = max(res, (ord('a') + 26 - ord(c)) % 26)
        return res

