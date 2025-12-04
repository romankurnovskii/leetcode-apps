## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** `left` and `right` range from 0 to 2^31 - 1, with `left <= right`.
- **Time Complexity:** O(log n) where n is the maximum of left and right. We shift bits until left equals right.
- **Space Complexity:** O(1) - We use only a constant amount of extra space.
- **Edge Case:** If `left == right`, the result is `left` itself.

**1.2 High-level approach:**
The goal is to find the bitwise AND of all numbers in a range. The key insight is that the result is the common prefix of `left` and `right` in binary representation, with all remaining bits set to 0.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Iterate through all numbers from `left` to `right` and compute their AND. This is O(n) where n is the range size, which can be very large.
- **Optimized Strategy:** Find the common prefix by right-shifting both numbers until they're equal, then left-shift back. This is O(log n) time.
- **Why optimized is better:** We avoid iterating through potentially millions of numbers and directly compute the result from the common prefix.

**1.4 Decomposition:**
1. Right-shift both `left` and `right` until they become equal (finding the common prefix).
2. Count how many times we shifted (stored in `shift`).
3. Left-shift the common value back by `shift` positions to restore the common prefix with trailing zeros.
4. Return the result.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `left = 5` (binary: `101`), `right = 7` (binary: `111`)

Initialize `shift = 0`.

**2.2 Start Checking:**
Right-shift both numbers until they're equal.

**2.3 Trace Walkthrough:**

| Iteration | left | right | left < right? | Action |
|-----------|------|-------|---------------|--------|
| 0 | 5 (101) | 7 (111) | Yes | Shift both: left=2, right=3, shift=1 |
| 1 | 2 (10) | 3 (11) | Yes | Shift both: left=1, right=1, shift=2 |
| 2 | 1 (1) | 1 (1) | No | Stop, common prefix is 1 |

**2.4 Increment and Loop:**
While `left < right`:
- Right-shift both: `left >>= 1`, `right >>= 1`
- Increment `shift`

**2.5 Return Result:**
Common prefix is `1`, shift back: `1 << 2 = 4` (binary: `100`). This is the bitwise AND of [5, 6, 7] because the common prefix is `1` and all other bits differ.

