## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `s.length == indices.length == n`, `1 <= n <= 100`.
- **Characters:** `s` consists of only lowercase English letters.
- **Time Complexity:** O(n) - we iterate through the string once to place each character.
- **Space Complexity:** O(n) - we create a result array of length n.
- **Edge Case:** If indices are already in order [0, 1, 2, ..., n-1], return the original string.

**1.2 High-level approach:**

The goal is to restore the original string by placing each character at the position specified by the indices array. We create a result array and place each character from the original string at its target index.

![Visualization showing how characters are moved from their original positions to new positions based on the indices array]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try to swap characters in place, which can be complex and error-prone.
- **Optimized Strategy:** Create a new array and directly place each character at its target index. This is straightforward and efficient.
- **Why it's better:** The direct placement approach is simple, clear, and runs in O(n) time with O(n) space, which is optimal for this problem.

**1.4 Decomposition:**

1. Create a result array of the same length as the string, initialized with empty strings.
2. For each character in the original string at index i, place it at position `indices[i]` in the result array.
3. Join the result array into a string and return it.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "codeleet"`, `indices = [4, 5, 6, 7, 0, 2, 1, 3]`.

We initialize:
- `res = ['', '', '', '', '', '', '', '']` (8 empty strings)

**2.2 Start Checking:**

Place each character at its target index.

**2.3 Trace Walkthrough:**

| Step | i | s[i] | indices[i] | res after placement |
|------|---|------|------------|---------------------|
| 1 | 0 | 'c' | 4 | ['', '', '', '', 'c', '', '', ''] |
| 2 | 1 | 'o' | 5 | ['', '', '', '', 'c', 'o', '', ''] |
| 3 | 2 | 'd' | 6 | ['', '', '', '', 'c', 'o', 'd', ''] |
| 4 | 3 | 'e' | 7 | ['', '', '', '', 'c', 'o', 'd', 'e'] |
| 5 | 4 | 'l' | 0 | ['l', '', '', '', 'c', 'o', 'd', 'e'] |
| 6 | 5 | 'e' | 2 | ['l', '', 'e', '', 'c', 'o', 'd', 'e'] |
| 7 | 6 | 'e' | 1 | ['l', 'e', 'e', '', 'c', 'o', 'd', 'e'] |
| 8 | 7 | 't' | 3 | ['l', 'e', 'e', 't', 'c', 'o', 'd', 'e'] |

After all placements:
- `res = ['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']`
- Joined: `"leetcode"`

**2.4 Increment and Loop:**

Continue until all characters are placed.

**2.5 Return Result:**

Return `res = "leetcode"` - the restored string.

