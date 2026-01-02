## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to find the maximum partition factor, where the factor is the ratio of left sum to right sum at a partition point.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n) - we iterate through possible partition points once, where n is the array length.
- **Space Complexity:** O(1) - we only need variables to track sums.
- **Edge Case:** If right sum is 0, the factor is undefined (we skip). If all elements are 0, all partitions have undefined factors.

**1.2 High-level approach:**

The goal is to try each partition position, calculate left sum and right sum, and find the maximum ratio.

![Partition factor visualization](https://assets.leetcode.com/static_assets/others/partition-factor.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate sums for each partition independently. This is O(n^2).
- **Optimized Strategy:** Pre-calculate total sum, then for each partition, calculate left sum incrementally and right sum from total. This is O(n) time.
- **Optimization:** By using incremental calculation, we avoid recalculating sums and solve in linear time.

**1.4 Decomposition:**

1. Calculate total sum of the array.
2. Initialize left sum to 0.
3. For each partition position from 1 to n-1:
   - Update left sum by adding current element.
   - Calculate right sum = total - left sum.
   - If right sum != 0, calculate factor = left sum / right sum.
   - Update maximum factor.
4. Return the maximum factor.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 3, 4]`

- Total sum: `10`
- Left sum: `0`
- Result variable: `res = 1`

**2.2 Start Checking:**

We try each partition position.

**2.3 Trace Walkthrough:**

| Step | Partition | Left sum | Right sum | Factor | res |
| ---- | --------- | -------- | --------- | ------ | --- |
| 1    | After 1 | 1 | 9 | 1/9 | 1 |
| 2    | After 2 | 3 | 7 | 3/7 | 3/7 |
| 3    | After 3 | 6 | 4 | 6/4 = 1.5 | 1.5 |

**2.4 Increment and Loop:**

After each partition, we calculate the factor and update the maximum.

**2.5 Return Result:**

The result is `1.5`, which is the maximum partition factor (when left = [1,2,3] and right = [4]).

