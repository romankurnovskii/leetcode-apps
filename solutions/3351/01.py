class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        from collections import Counter

        # Count frequency of each character
        count = Counter(s)
        max_freq = max(count.values())

        # Find characters with maximum frequency
        max_chars = [char for char, freq in count.items() if freq == max_freq]

        # Find last occurrence of each max frequency character
        last_positions = {}
        for i, char in enumerate(s):
            if char in max_chars:
                last_positions[char] = i

        # Sort by last position and build result
        sorted_chars = sorted(max_chars, key=lambda x: last_positions[x])
        res = "".join(sorted_chars)

        return res
