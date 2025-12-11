from collections import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        # Try all possible substrings
        for i in range(n):
            char_count = Counter()

            for j in range(i, n):
                char_count[s[j]] += 1

                # Get distinct characters and their counts
                distinct_chars = list(char_count.keys())
                if len(distinct_chars) == 0:
                    continue

                # Check if all distinct characters appear the same number of times
                counts = [char_count[c] for c in distinct_chars]
                if len(set(counts)) == 1:  # All counts are equal
                    res = max(res, j - i + 1)

        return res
