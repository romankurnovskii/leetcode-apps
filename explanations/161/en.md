## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to determine if two strings are exactly one edit distance apart. An edit can be: inserting one character, deleting one character, or replacing one character. The strings must differ by exactly one operation, not zero or more than one.

**1.1 Constraints & Complexity:**
- Input size: `0 <= s.length, t.length <= 10^4`
- **Time Complexity:** O(n) where n is the length of the shorter string - we compare characters until we find a difference
- **Space Complexity:** O(1) - we only use a few variables, no extra data structures
- **Edge Case:** If both strings are empty, they are zero edit distance apart, return False. If one string is empty and the other has one character, return True.

**1.2 High-level approach:**
We first check if the length difference is more than 1 (impossible to be one edit). Then we compare characters from the start. When we find the first difference, we check if the remaining substrings match based on whether the strings have the same length (replacement) or different lengths (insertion/deletion).

![Comparing strings character by character](https://assets.leetcode.com/static_assets/others/one-edit-distance.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible single edits (insert, delete, replace) and check if any results in the target string. This is O(n²) or worse.
- **Optimized Strategy:** Compare strings character by character, and when we find a difference, check if the remaining parts match. This is O(n) time.
- **Why it's better:** We only need one pass through the strings, stopping as soon as we can determine the answer.

**1.4 Decomposition:**
1. Check if length difference is more than 1 - if so, return False
2. Ensure s is the shorter string (swap if needed for easier logic)
3. Compare characters from the start until we find a difference
4. If lengths are equal, check if remaining substrings match (replacement case)
5. If lengths differ by 1, check if remaining substring of longer matches remaining of shorter (insertion/deletion case)

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "ab"`, `t = "acb"`
- `len_s = 2`, `len_t = 3`
- Length difference is 1, so it's possible
- Swap to make s shorter: `s = "ab"`, `t = "acb"` (already correct)

**2.2 Start Checking:**
We begin comparing characters from index 0.

**2.3 Trace Walkthrough:**

| i | s[i] | t[i] | Match? | Action |
|---|------|------|--------|--------|
| 0 | 'a' | 'a' | Yes | Continue |
| 1 | 'b' | 'c' | No | Check remaining |

At i=1, we found a difference. Since `len_s < len_t`:
- Check if `s[1:] == t[2:]` → `"b" == "b"` → True
- This means 'c' was inserted in t, so return True

**Another example:** `s = "ab"`, `t = "ac"`
- At i=1: `s[1:] == "b"`, `t[1:] == "c"`
- Since lengths are equal, check `s[1:] == t[1:]` → `"b" == "c"` → False
- This means it's a replacement, but the remaining parts don't match, so return False

**2.4 Increment and Loop:**
We increment i as we compare characters. When we find a mismatch, we stop and check the remaining parts.

**2.5 Return Result:**
Return True if exactly one edit is found (remaining parts match after the difference), False otherwise. For `s = "ab"`, `t = "acb"`, we return True because one insertion makes them equal.

