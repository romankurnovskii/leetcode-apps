from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # dp[i] represents if s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented

        for i in range(1, n + 1):
            for j in range(i):
                # If s[0:j] can be segmented and s[j:i] is in wordDict
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
