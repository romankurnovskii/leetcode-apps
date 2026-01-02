## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a string and an integer k, we need to find the lexicographically smallest string by changing at most k characters, where each change has a circular cost (distance in alphabet).

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 100, and k can be up to 100.
- **Time Complexity:** O(n * 26) where n is the string length - for each position, we try up to 26 characters.
- **Space Complexity:** O(n) - we need to store the result string.
- **Edge Case:** If k is 0, return the original string. If k is very large, we can change all characters to 'a'.

**1.2 High-level approach:**

The goal is to greedily change each character to the smallest possible character ('a') while staying within the k budget, considering circular distance in the alphabet.

![Lexicographic optimization visualization](https://assets.leetcode.com/static_assets/others/lex-optimize.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible character changes. This is exponential.
- **Optimized Strategy:** Greedily change each character to the smallest possible character within budget. This is O(n * 26) time.
- **Optimization:** By processing left to right and always choosing the smallest character within budget, we get the lexicographically smallest result.

**1.4 Decomposition:**

1. Convert string to list for modification.
2. For each character position:
   - Try characters from 'a' to current character.
   - Calculate circular distance cost.
   - Choose the smallest character that fits in remaining budget.
3. Update k budget after each change.
4. Return the modified string.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "zab"`, `k = 2`

- String list: `['z', 'a', 'b']`
- Budget: `k = 2`
- Result variable: `res = []`

**2.2 Start Checking:**

We process each character position.

**2.3 Trace Walkthrough:**

| Step | Pos | Char | Try | Cost | Budget | Action | Result |
| ---- | --- | ---- | --- | ---- | ------ | ------ | ------ |
| 1    | 0 | 'z' | 'a' | 1 | 2 | Change to 'a' | ['a'] |
| 2    | 1 | 'a' | 'a' | 0 | 1 | Already 'a' | ['a','a'] |
| 3    | 2 | 'b' | 'a' | 1 | 1 | Change to 'a' | ['a','a','a'] |

**2.4 Increment and Loop:**

After each position, we update the budget and continue.

**2.5 Return Result:**

The result is `"aaa"`, which is the lexicographically smallest string achievable with k=2.

