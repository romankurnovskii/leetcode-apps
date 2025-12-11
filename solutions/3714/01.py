class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        # P[i] = (a_i, b_i, c_i) = count of 'a', 'b', 'c' in s[:i]
        P = [[0, 0, 0]]
        for c in s:
            P.append(P[-1][:])
            if c == "a":
                P[-1][0] += 1
            elif c == "b":
                P[-1][1] += 1
            else:  # c == 'c'
                P[-1][2] += 1

        res = 0
        first = {}

        for i, (a, b, c) in enumerate(P):
            # Case 1: All 3 characters balanced: a-b and a-c must be same
            key1 = ("abc", a - b, a - c)
            res = max(res, i - first.get(key1, i))
            first.setdefault(key1, i)

            # Case 2: Only 'a' and 'b' balanced: a-b must be same, c must be same
            key2 = ("ab", a - b, c)
            res = max(res, i - first.get(key2, i))
            first.setdefault(key2, i)

            # Case 3: Only 'b' and 'c' balanced: b-c must be same, a must be same
            key3 = ("bc", b - c, a)
            res = max(res, i - first.get(key3, i))
            first.setdefault(key3, i)

            # Case 4: Only 'c' and 'a' balanced: c-a must be same, b must be same
            key4 = ("ca", c - a, b)
            res = max(res, i - first.get(key4, i))
            first.setdefault(key4, i)

            # Case 5: Only 'a' (single character)
            key5 = ("a", b, c)
            res = max(res, i - first.get(key5, i))
            first.setdefault(key5, i)

            # Case 6: Only 'b' (single character)
            key6 = ("b", c, a)
            res = max(res, i - first.get(key6, i))
            first.setdefault(key6, i)

            # Case 7: Only 'c' (single character)
            key7 = ("c", a, b)
            res = max(res, i - first.get(key7, i))
            first.setdefault(key7, i)

        return res
