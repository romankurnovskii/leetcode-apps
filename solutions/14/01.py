from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        # Find the minimum length to avoid index out of bounds
        min_len = min(len(s) for s in strs)

        res = ""
        for i in range(min_len):
            # Get the character from the first string at position i
            char = strs[0][i]

            # Check if all other strings have the same character at position i
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return res

            # If all strings have the same character, add it to result
            res += char

        return res
