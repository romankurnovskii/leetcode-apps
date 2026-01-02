## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of integers, we need to find the maximum score of a split, where the score is the sum of the left part plus the sum of the right part.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^5 elements.
- **Time Complexity:** O(n) - we calculate prefix sums in O(n) and then iterate once to find the maximum, where n is the array length.
- **Space Complexity:** O(n) - we need to store prefix sums.
- **Edge Case:** If the array has length 2, there's only one split. If all numbers are negative, we need to find the best split carefully.

**1.2 High-level approach:**

The goal is to try each possible split position and calculate the sum of left and right parts, then return the maximum.

![Array split visualization](https://assets.leetcode.com/static_assets/others/array-split.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each split, calculate left sum and right sum separately. This is O(n^2).
- **Optimized Strategy:** Pre-calculate prefix sums, then for each split, get left sum from prefix and right sum from total minus prefix. This is O(n) time.
- **Optimization:** By using prefix sums, we avoid recalculating sums for each split and solve in linear time.

**1.4 Decomposition:**

1. Calculate prefix sums for the array.
2. Calculate total sum of the array.
3. For each split position from 1 to n-1:
   - Left sum = prefix_sum[i]
   - Right sum = total_sum - prefix_sum[i]
   - Score = left_sum + right_sum
   - Update maximum score.
4. Return the maximum score.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 3, 4, 5]`

- Prefix sums: `[0, 1, 3, 6, 10, 15]`
- Total sum: `15`
- Result variable: `res = 0`

**2.2 Start Checking:**

We try each split position.

**2.3 Trace Walkthrough:**

| Step | Split | Left sum | Right sum | Score | res |
| ---- | ----- | -------- | --------- | ----- | --- |
| 1    | After 1 | 1 | 14 | 15 | 15 |
| 2    | After 2 | 3 | 12 | 15 | 15 |
| 3    | After 3 | 6 | 9 | 15 | 15 |
| 4    | After 4 | 10 | 5 | 15 | 15 |

**2.4 Increment and Loop:**

After each split, we calculate the score and update the maximum.

**2.5 Return Result:**

The result is `15`, which is the maximum score (actually all splits give the same score when we sum left + right, as it equals the total sum).
