from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        
        res = 0
        # Count characters that need to be changed in t
        for char in count_s:
            if count_t[char] < count_s[char]:
                res += count_s[char] - count_t[char]
        
        return res
