class Solution:
    def maxDistinct(self, s: str) -> int:
        # Count distinct characters in the string
        # Each substring must start with a distinct character
        # So the answer is the number of distinct characters
        distinct_chars = len(set(s))
        return distinct_chars
