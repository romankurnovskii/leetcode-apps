class Solution:
    def maxDistinct(self, s: str) -> int:
        # The maximum number of substrings equals the number of distinct characters
        # Each character can only start one substring
        return len(set(s))

