class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)

        # Use Z-algorithm to find longest suffix which is also a prefix
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z

        z = z_function(word)

        # Find the minimum time
        # After t seconds, we've removed t*k characters
        # The remaining suffix (n - t*k) must match the prefix
        for t in range(1, (n + k - 1) // k + 1):
            removed = t * k
            if removed >= n:
                return t
            # Check if suffix starting at 'removed' matches prefix
            suffix_start = removed
            if z[suffix_start] >= n - removed:
                return t

        return (n + k - 1) // k
