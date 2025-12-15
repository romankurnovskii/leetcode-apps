class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)

        res = 0
        for char in count_s:
            if count_s[char] > count_t[char]:
                res += count_s[char] - count_t[char]

        return res
