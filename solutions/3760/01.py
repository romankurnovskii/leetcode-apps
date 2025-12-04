class Solution:
    def maxDistinct(self, s: str) -> int:
        # The maximum number of substrings equals the number of distinct characters
        # Each substring must start with a distinct character
        res = len(set(s))
        return res
