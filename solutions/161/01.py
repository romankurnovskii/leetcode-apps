class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)

        if abs(len_s - len_t) > 1:
            return False

        if len_s > len_t:
            s, t = t, s
            len_s, len_t = len_t, len_s

        for i in range(len_s):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i + 1 :] == t[i + 1 :]
                else:
                    return s[i:] == t[i + 1 :]

        return len_s + 1 == len_t
