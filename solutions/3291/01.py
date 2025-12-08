class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        # dp[i] = minimum valid strings to form target[0:i]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # Build set of all possible prefixes from words
        prefixes = set()
        for word in words:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])

        # DP: for each position, try all matching prefixes
        for i in range(n):
            if dp[i] == float("inf"):
                continue

            for j in range(i + 1, n + 1):
                substr = target[i:j]
                if substr in prefixes:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[n] if dp[n] != float("inf") else -1
