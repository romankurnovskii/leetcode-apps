class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by spaces and filter out empty strings
        words = s.split()
        # Reverse the list and join with spaces
        return ' '.join(reversed(words))
