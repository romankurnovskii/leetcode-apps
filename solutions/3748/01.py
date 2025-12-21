class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        n = len(s)

        # Find all x such that x^2 % k == 0
        valid_x = []
        for x in range(1, n + 1):
            if (x * x) % k == 0:
                valid_x.append(x)

        # Build prefix sum for vowels and consonants
        # Use +1 for vowel, -1 for consonant
        prefix = [0]
        for char in s:
            if char in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1] - 1)

        res = 0
        # For each valid x, count substrings with vowels == consonants == x
        for x in valid_x:
            # We need substrings of length 2*x with prefix difference = 0
            count_map = {}
            for i in range(len(prefix)):
                # Look for prefix[j] such that prefix[i] - prefix[j] == 0
                # and length is 2*x
                if i >= 2 * x:
                    prev_prefix = prefix[i - 2 * x]
                    count_map[prev_prefix] = count_map.get(prev_prefix, 0) + 1

                # Count matches
                res += count_map.get(prefix[i], 0)

        return res
