class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        # dp[i] = minimum valid strings to form target[0:i]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # Build Trie of all possible prefixes from words
        from collections import defaultdict

        class TrieNode:
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.is_end = False

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
                node.is_end = True  # Mark all prefixes as valid

        # DP: for each position, try all matching prefixes using Trie
        for i in range(n):
            if dp[i] == float("inf"):
                continue

            # Use Trie to find all matching prefixes starting at position i
            node = root
            for j in range(i, n):
                if target[j] not in node.children:
                    break
                node = node.children[target[j]]
                if node.is_end:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)

        return dp[n] if dp[n] != float("inf") else -1
