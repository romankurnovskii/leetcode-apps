class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)
        # dp[i] = minimum cost to construct target[0:i]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float("inf"):
                continue

            # Try each word
            for j, word in enumerate(words):
                word_len = len(word)
                if i + word_len <= n and target[i : i + word_len] == word:
                    dp[i + word_len] = min(dp[i + word_len], dp[i] + costs[j])

        return dp[n] if dp[n] != float("inf") else -1
