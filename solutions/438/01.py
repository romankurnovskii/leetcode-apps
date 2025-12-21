class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        # Count characters in p
        p_count = {}
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1

        # Sliding window
        window_count = {}
        res = []
        left = 0

        for right in range(len(s)):
            # Add right character
            window_count[s[right]] = window_count.get(s[right], 0) + 1

            # If window size equals p length, check if it's an anagram
            if right - left + 1 == len(p):
                if window_count == p_count:
                    res.append(left)

                # Remove left character
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1

        return res
