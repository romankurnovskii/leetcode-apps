## Explanation

### Strategy (The "Why")

Given two strings `s` and `t`, we need to determine if `s` is a subsequence of `t`. A subsequence means that characters of `s` appear in `t` in the same order, but not necessarily consecutively.

**1.1 Constraints & Complexity:**

- **Input Size:** The string lengths can be up to $10^4$.
- **Value Range:** Strings contain only lowercase English letters.
- **Time Complexity:** $O(n)$ where $n$ is the length of `t`. We iterate through `t` once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for pointers.
- **Edge Case:** If `s` is empty, it's always a subsequence of any string (empty string is a subsequence of any string).

**1.2 High-level approach:**

The goal is to check if all characters of `s` appear in `t` in the same order.

We use two pointers: one for `s` and one for `t`. We traverse `t` and whenever we find a character matching the current character in `s`, we advance the pointer in `s`.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subsequences of `t` and check if any equals `s`. This would be exponential.
- **Optimized Strategy (Two Pointers):** Use two pointers to traverse both strings simultaneously. This takes $O(n)$ time.
- **Why it's better:** The two-pointer approach is optimal and straightforward, checking characters in order without generating all possible subsequences.

**1.4 Decomposition:**

1. Initialize two pointers: one for `s` (starting at 0) and one for `t` (starting at 0).
2. Traverse `t` with the pointer.
3. Whenever we find a character in `t` that matches the current character in `s`, advance the pointer in `s`.
4. After traversing `t`, check if we've matched all characters in `s` (pointer equals length of `s`).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "abc"$, $t = "ahbgdc"$

We initialize:
- `i = 0` (pointer for `s`)
- `j = 0` (pointer for `t`)

**2.2 Start Checking:**

We begin traversing `t`.

**2.3 Trace Walkthrough:**

| j | t[j] | i | s[i] | Match? | Action | i After |
|---|------|---|------|--------|--------|---------|
| 0 | 'a' | 0 | 'a' | Yes | Advance i | 1 |
| 1 | 'h' | 1 | 'b' | No | Continue | 1 |
| 2 | 'b' | 1 | 'b' | Yes | Advance i | 2 |
| 3 | 'g' | 2 | 'c' | No | Continue | 2 |
| 4 | 'd' | 2 | 'c' | No | Continue | 2 |
| 5 | 'c' | 2 | 'c' | Yes | Advance i | 3 |

**2.4 Check Result:**

After traversing `t`, `i = 3` which equals `len(s) = 3`, so all characters were matched.

**2.5 Return Result:**

We return `True` because `s` is a subsequence of `t`.

> **Note:** The key insight is that we only need to check if characters of `s` appear in `t` in order. We don't need to check all possible subsequences - we can greedily match the first occurrence of each character in `s` as we traverse `t`.
