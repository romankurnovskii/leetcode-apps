## Explanation

### Strategy (The "Why")

Given two strings `s` and `t`, we need to return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such window, return the empty string.

**1.1 Constraints & Complexity:**

- **Input Size:** The string lengths can be up to $10^5$.
- **Value Range:** Strings contain uppercase and lowercase English letters.
- **Time Complexity:** $O(|s| + |t|)$ - We use sliding window that processes each character in `s` at most twice (once when expanding, once when shrinking).
- **Space Complexity:** $O(|s| + |t|)$ - We use hash maps to count characters in `t` and the current window.
- **Edge Case:** If `t` is longer than `s`, return empty string. If `s` doesn't contain all characters of `t`, return empty string.

**1.2 High-level approach:**

The goal is to find the shortest substring of `s` that contains all characters of `t`.

We use a sliding window approach. We expand the window until it contains all characters of `t`, then shrink it from the left while maintaining the property, tracking the minimum window.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible substrings and check if they contain all characters of `t`. This takes $O(|s|^2 \times |t|)$ time.
- **Optimized Strategy (Sliding Window):** Use two pointers to maintain a window that contains all characters of `t`. This takes $O(|s| + |t|)$ time.
- **Why it's better:** The sliding window approach reduces time complexity by maintaining a valid window and only moving pointers forward, avoiding the need to check all substrings.

**1.4 Decomposition:**

1. Count characters needed from `t`.
2. Use two pointers (left and right) to maintain a sliding window.
3. Expand the window by moving the right pointer until all characters of `t` are included.
4. Shrink the window from the left while maintaining the property, tracking the minimum window.
5. Return the minimum window substring.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "ADOBECODEBANC"$, $t = "ABC"$

We initialize:
- `need = {'A': 1, 'B': 1, 'C': 1}`
- `window = {}`
- `left = 0`, `right = 0`
- `valid = 0`
- `min_len = \infty`

**2.2 Start Sliding Window:**

We begin expanding the window.

**2.3 Trace Walkthrough:**

| right | s[right] | window | valid | Action | left | min_len |
|-------|----------|--------|-------|--------|------|---------|
| 0 | 'A' | {'A':1} | 1 | Continue | 0 | $\infty$ |
| 1 | 'D' | {'A':1} | 1 | Continue | 0 | $\infty$ |
| 2 | 'O' | {'A':1} | 1 | Continue | 0 | $\infty$ |
| 3 | 'B' | {'A':1,'B':1} | 2 | Continue | 0 | $\infty$ |
| 4 | 'E' | {'A':1,'B':1} | 2 | Continue | 0 | $\infty$ |
| 5 | 'C' | {'A':1,'B':1,'C':1} | 3 | Shrink | 0 | 6 |
| ... | ... | ... | ... | ... | ... | ... |

**2.4 Minimum Window:**

- First valid window: "ADOBEC" (length 6)
- After shrinking: "BANC" (length 4) - minimum!

**2.5 Return Result:**

We return "BANC", which is the minimum window containing all characters of `t`.

> **Note:** The key insight is to use a sliding window that expands until it contains all required characters, then shrinks from the left to find the minimum window. We track how many distinct characters have the required count using a `valid` counter.

