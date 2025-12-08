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
        for i in range(1, n):
            # Check if word[i:] is a prefix of word
            if z[i] == n - i:
                # Check if length is multiple of k
                if (n - i) % k == 0:
                    return (n - i) // k

        # If no suffix-prefix match, return ceil(n/k)
        return (n + k - 1) // k
