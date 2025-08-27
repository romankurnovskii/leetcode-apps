class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from the end of the string
        i = len(s) - 1
        length = 0

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count characters of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        # Return the length of the last word
        return length
