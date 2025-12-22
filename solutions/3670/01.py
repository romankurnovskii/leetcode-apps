class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # dp[i] = longest suffix of word2 that exists as subsequence
        # starting from index i in word1
        dp = [0] * (n + 1)

        # Build dp from right to left
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            # Check if we can extend the subsequence
            if dp[i] < m and word1[i] == word2[m - 1 - dp[i]]:
                dp[i] += 1

        # If no valid sequence exists
        if dp[0] < m:
            return []

        # Greedily build the lexicographically smallest sequence
        res = []
        pos = 0  # position in word1
        target_pos = 0  # position in word2

        while target_pos < m:
            # Find the leftmost character that can form a valid sequence
            for i in range(pos, n):
                if word1[i] == word2[target_pos]:
                    # Check if we can complete the sequence from i+1
                    if dp[i + 1] >= m - target_pos - 1:
                        res.append(i)
                        pos = i + 1
                        target_pos += 1
                        break

        return res
