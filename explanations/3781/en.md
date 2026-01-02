## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a binary string, we need to find the maximum score after splitting it into two non-empty substrings. The score is the sum of zeros in the left substring and ones in the right substring.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 500.
- **Time Complexity:** O(n) - we iterate through the string once to count total ones, then once more to find the best split, where n is the string length.
- **Space Complexity:** O(1) - we only need a few variables to track counts.
- **Edge Case:** If the string has length 2, there's only one possible split. If all characters are the same, the score depends on the split position.

**1.2 High-level approach:**

The goal is to try each possible split position and calculate the score (left zeros + right ones), then return the maximum score.

![String splitting visualization](https://assets.leetcode.com/static_assets/others/string-split.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each split position, count zeros in left and ones in right. This is O(n^2) if we count naively.
- **Optimized Strategy:** Pre-count total ones, then for each split, track left zeros and calculate right ones from total. This is O(n) time.
- **Optimization:** By pre-counting and using incremental updates, we avoid redundant counting and solve in linear time.

**1.4 Decomposition:**

1. Count the total number of ones in the string.
2. Initialize variables to track left zeros and left ones.
3. For each split position (from 1 to n-1):
   - Update left zeros and left ones.
   - Calculate right ones = total ones - left ones.
   - Calculate score = left zeros + right ones.
   - Update maximum score.
4. Return the maximum score.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "011101"`

- Total ones: `4`
- Left zeros: `left_zeros = 0`
- Left ones: `left_ones = 0`
- Result variable: `res = 0`

**2.2 Start Checking:**

We try each split position from index 1 to n-1.

**2.3 Trace Walkthrough:**

| Step | Split | Left | Right | left_zeros | right_ones | Score | res |
| ---- | ----- | ---- | ----- | ---------- | ---------- | ----- | --- |
| 1    | After 0 | "0" | "11101" | 1 | 4 | 5 | 5 |
| 2    | After 01 | "01" | "1101" | 1 | 3 | 4 | 5 |
| 3    | After 011 | "011" | "101" | 1 | 2 | 3 | 5 |
| 4    | After 0111 | "0111" | "01" | 1 | 1 | 2 | 5 |
| 5    | After 01110 | "01110" | "1" | 1 | 1 | 2 | 5 |

**2.4 Increment and Loop:**

After each split, we update counts and check if the score is better.

**2.5 Return Result:**

The result is `5`, which is the maximum score achieved by splitting after the first character ("0" | "11101").
