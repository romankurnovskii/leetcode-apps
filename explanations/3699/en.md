## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to find the length of the longest zigzag subsequence, where zigzag means elements alternate between increasing and decreasing.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n) - we iterate through the array once, where n is the array length.
- **Space Complexity:** O(1) - we only need variables to track the current state.
- **Edge Case:** If the array has length 1, return 1. If all elements are equal, return 1.

**1.2 High-level approach:**

The goal is to traverse the array and count how many times the direction changes (from increasing to decreasing or vice versa).

![Zigzag subsequence visualization](https://assets.leetcode.com/static_assets/others/zigzag-seq.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible subsequences. This is exponential.
- **Optimized Strategy:** Greedily build the longest zigzag by following the pattern. This is O(n) time.
- **Optimization:** By processing left to right and tracking direction changes, we find the longest zigzag efficiently.

**1.4 Decomposition:**

1. If array length < 2, return length.
2. Initialize count to 1 (first element).
3. For each position from 1 to n-1:
   - Check if current element maintains zigzag pattern with previous.
   - If yes, increment count.
4. Return count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 1, 3, 2]`

- Array: `[1, 2, 1, 3, 2]`
- Result variable: `res = 1`

**2.2 Start Checking:**

We check each element for zigzag pattern.

**2.3 Trace Walkthrough:**

| Step | i | nums[i] | Pattern | Follows? | res |
| ---- | - | ------- | ------- | -------- | --- |
| 1    | 0 | 1 | - | Start | 1 |
| 2    | 1 | 2 | Up | Yes | 2 |
| 3    | 2 | 1 | Down | Yes | 3 |
| 4    | 3 | 3 | Up | Yes | 4 |
| 5    | 4 | 2 | Down | Yes | 5 |

**2.4 Increment and Loop:**

After each element, we check if it maintains the zigzag pattern.

**2.5 Return Result:**

The result is `5`, which is the length of the longest zigzag subsequence (the entire array in this case).

