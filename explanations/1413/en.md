## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of integers, we need to find the minimum positive starting value such that when we add the array elements step by step, the cumulative sum is always positive.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 100 elements, with each element between -100 and 100.
- **Time Complexity:** O(n) - we iterate through the array once to calculate prefix sums and find the minimum, where n is the array length.
- **Space Complexity:** O(1) - we only need to track the minimum prefix sum, not store all prefix sums.
- **Edge Case:** If all elements are positive, the starting value is 1. If the minimum prefix sum is 0, we need starting value 1. If it's negative, we need 1 - min_sum.

**1.2 High-level approach:**

The goal is to calculate the prefix sums and find the minimum value. The starting value must be at least 1 - min_prefix_sum to ensure all prefix sums are positive.

![Prefix sum visualization](https://assets.leetcode.com/static_assets/others/prefix-sum.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try different starting values until we find one that works. This could require many iterations.
- **Optimized Strategy:** Calculate prefix sums once, find the minimum, and compute the required starting value directly. This is O(n) time.
- **Optimization:** By calculating prefix sums and finding the minimum in one pass, we can determine the answer directly without trying multiple values.

**1.4 Decomposition:**

1. Initialize variables to track the current prefix sum and the minimum prefix sum.
2. Iterate through the array, adding each element to the prefix sum.
3. Update the minimum prefix sum if the current prefix sum is smaller.
4. Calculate the starting value as 1 - min_prefix_sum (ensuring it's at least 1).
5. Return the starting value.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [-3, 2, -3, 4, 2]`

- Array: `[-3, 2, -3, 4, 2]`
- Prefix sum: `prefix_sum = 0`
- Minimum prefix sum: `min_sum = 0`

**2.2 Start Checking:**

We begin calculating prefix sums step by step.

**2.3 Trace Walkthrough:**

| Step | Element | prefix_sum before | prefix_sum after | min_sum |
| ---- | ------- | ----------------- | ---------------- | ------- |
| 1    | -3      | 0                 | -3               | -3      |
| 2    | 2       | -3                | -1               | -3      |
| 3    | -3      | -1                | -4               | -4      |
| 4    | 4       | -4                | 0                | -4      |
| 5    | 2       | 0                 | 2                | -4      |

**2.4 Increment and Loop:**

After processing each element, we update the minimum and continue.

**2.5 Return Result:**

The minimum prefix sum is -4, so the starting value must be at least 1 - (-4) = 5. The result is `5`.

