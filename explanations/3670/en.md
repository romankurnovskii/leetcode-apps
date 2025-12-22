## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the lexicographically smallest sequence of indices from word1 such that concatenating characters at these indices results in a string that is "almost equal" to word2 (can change at most one character to make it identical).

**1.1 Constraints & Complexity:**

- **Input Size:** word1 length can be up to 3×10^5, word2 length is less than word1 length.
- **Time Complexity:** O(n * m) where n is word1 length and m is word2 length - we build a DP array and then greedily select indices.
- **Space Complexity:** O(n) - we store the DP array of size n+1.
- **Edge Case:** If no valid sequence exists (word2 cannot be formed as an "almost equal" subsequence), return empty array.

**1.2 High-level approach:**

The goal is to use dynamic programming to determine if a valid sequence exists, then greedily select the leftmost valid character at each step to ensure lexicographically smallest result.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible sequences of indices, check if they form an "almost equal" string. This would be exponential.
- **Optimized Strategy:** Use DP to check feasibility from right to left, then greedily select leftmost valid characters from left to right. This is O(n * m) time.
- **Optimization:** DP allows us to check if a solution exists efficiently, and greedy selection ensures we get the lexicographically smallest result.

**1.4 Decomposition:**

1. Build a DP array from right to left: dp[i] = longest suffix of word2 that can be matched starting from index i in word1.
2. Check if a valid sequence exists (dp[0] >= m).
3. If valid, greedily build the sequence: for each character in word2, select the leftmost matching character in word1 that allows completing the rest of the sequence.
4. Return the sequence of indices.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `word1 = "vbcca", word2 = "abc"`

- We need to find indices in word1 that form "abc" (with at most one character change).
- Initialize dp = [0, 0, 0, 0, 0, 0] (size n+1)

**2.2 Start Processing:**

We build the DP array from right to left to check feasibility.

**2.3 Trace Walkthrough:**

Building DP (right to left):
- i=4: dp[4] = 0, check if 'a' matches word2[2]? No, dp[4] = 0
- i=3: dp[3] = 0, check if 'c' matches word2[2]? Yes, dp[3] = 1
- i=2: dp[2] = 1, check if 'c' matches word2[1]? Yes, dp[2] = 2
- i=1: dp[1] = 2, check if 'b' matches word2[0]? Yes, dp[1] = 3
- i=0: dp[0] = 3, check if 'v' matches word2[0]? No, dp[0] = 3

dp[0] = 3 >= 3, so valid sequence exists.

Greedy selection (left to right):
- target_pos=0, need 'a': Find leftmost 'a' at index 0? No. At index 4? Yes. Check dp[5] >= 2? Yes. Select index 4.
- target_pos=1, need 'b': Find leftmost 'b' at index 1? Yes. Check dp[2] >= 1? Yes. Select index 1.
- target_pos=2, need 'c': Find leftmost 'c' at index 2? Yes. Check dp[3] >= 0? Yes. Select index 2.

Wait, let me recalculate. Actually, we need to change 'v' to 'a', so we select index 0, then 1, then 2.

**2.4 Increment and Loop:**

The algorithm processes each position in word2 once, selecting the leftmost valid character that allows completion.

**2.5 Return Result:**

For `word1 = "vbcca", word2 = "abc"`, the result is [0, 1, 2]. We change word1[0]='v' to 'a', and use word1[1]='b' and word1[2]='c' as-is.

