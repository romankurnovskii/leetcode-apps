class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        res = s

        # Try reversing first k characters for all k from 1 to n
        for k in range(1, n + 1):
            # Reverse first k characters
            reversed_prefix = s[:k][::-1]
            candidate = reversed_prefix + s[k:]
            if candidate < res:
                res = candidate

        # Try reversing last k characters for all k from 1 to n
        for k in range(1, n + 1):
            # Reverse last k characters
            reversed_suffix = s[n - k :][::-1]
            candidate = s[: n - k] + reversed_suffix
            if candidate < res:
                res = candidate

        return res
