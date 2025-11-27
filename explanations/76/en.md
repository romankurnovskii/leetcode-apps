## Explanation

### Strategy (The "Why")

Given two strings `s` and `t`, we need to return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such window, return the empty string.

**1.1 Constraints & Complexity:**

- **Input Size:** The string lengths can be up to $10^5$.
- **Value Range:** Strings contain uppercase and lowercase English letters.
- **Time Complexity:** $O(|s| + |t|)$ - We use sliding window that processes each character in `s` at most twice (expand and shrink).
- **Space Complexity:** $O(|s| + |t|)$ - We use hash maps to count characters in `t` and the current window.
- **Edge Case:** If `t` is longer than `s`, return empty string. If `s` doesn't contain all characters of `t`, return empty string.

**1.2 High-level approach:**

The goal is to find the minimum window in `s` that contains all characters of `t`.

We use a sliding window approach. We expand the window until it contains all characters of `t`, then shrink it from the left to find the minimum window.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible substrings and check if they contain all characters of `t`. This takes $O(|s|^2 \times |t|)$ time.
- **Optimized Strategy (Sliding Window):** Use two pointers to maintain a window that contains all characters of `t`. This takes $O(|s| + |t|)$ time.
- **Why it's better:** The sliding window approach reduces time complexity by maintaining a valid window and only moving pointers forward, avoiding redundant checks.

**1.4 Decomposition:**

1. Count characters needed from `t`.
2. Use sliding window with two pointers.
3. Expand window by moving right pointer until all characters of `t` are included.
4. Shrink window by moving left pointer to find the minimum window.
5. Update minimum window whenever we find a valid window.
6. Return the minimum window substring.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "ADOBECODEBANC"$, $t = "ABC"$

We initialize:
- `need = {'A': 1, 'B': 1, 'C': 1}`
- `window = {}`
- `left = 0`, `right = 0`
- `valid = 0`

**2.2 Start Sliding Window:**

We begin expanding the window.

**2.3 Trace Walkthrough:**

| Step | right | s[right] | window | valid | Action | min_len |
|------|-------|----------|--------|-------|--------|---------|
| 1-5 | 0-4 | A-D-O-B-E | Build | 0-2 | Expand | - |
| 6 | 5 | C | Add C | 3 | **Valid!** | 6 |
| 7 | - | - | Shrink | 3 | Shrink left | 6 |
| 8-10 | 6-8 | O-D-E | Expand | 3 | Expand | 6 |
| 11 | 9 | B | Add B | 3 | **Valid!** | 4 |
| ... | ... | ... | ... | ... | ... | ... |

**2.4 Minimum Window:**

The minimum window found is "BANC" (indices 9-12, length 4).

**2.5 Return Result:**

We return "BANC", which is the minimum window substring containing all characters of "ABC".

> **Note:** The key insight is to use a sliding window that expands until it's valid, then shrinks to find the minimum. We track the number of characters that satisfy the requirement using a `valid` counter.

