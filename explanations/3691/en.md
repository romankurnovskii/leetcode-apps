## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to find the maximum value of any subarray.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n^2) - we check all possible subarrays, where n is the array length.
- **Space Complexity:** O(1) - we only need variables to track maximum.
- **Edge Case:** If the array is empty, return negative infinity. If all elements are negative, the maximum subarray is the single largest element.

**1.2 High-level approach:**

The goal is to check all possible subarrays and find the one with maximum sum (this is similar to maximum subarray problem but checking all subarrays).

![Subarray maximum visualization](https://assets.leetcode.com/static_assets/others/subarray-max.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all subarrays. This is O(n^2) which is acceptable for the constraints.
- **Optimized Strategy:** We could use Kadane's algorithm for maximum subarray, but the problem asks for checking all subarrays explicitly.
- **Optimization:** The O(n^2) approach is straightforward for the given constraints.

**1.4 Decomposition:**

1. For each starting position i:
   - Initialize current sum to 0.
   - For each ending position j >= i:
     - Add nums[j] to current sum.
     - Update maximum sum.
2. Return the maximum sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [-2, 1, -3, 4, -1, 2, 1]`

- Array: `[-2, 1, -3, 4, -1, 2, 1]`
- Result variable: `res = float('-inf')`

**2.2 Start Checking:**

We check all possible subarrays.

**2.3 Trace Walkthrough:**

| Step | Start | End | Subarray | Sum | res |
| ---- | ----- | --- | -------- | --- | --- |
| 1    | 0 | 0 | [-2] | -2 | -2 |
| 2    | 0 | 1 | [-2,1] | -1 | -1 |
| 3    | 3 | 3 | [4] | 4 | 4 |
| 4    | 3 | 6 | [4,-1,2,1] | 6 | 6 |
| ...  | ... | ... | ... | ... | 6 |

**2.4 Increment and Loop:**

After checking each subarray, we update the maximum.

**2.5 Return Result:**

The result is `6`, which is the maximum subarray sum (the subarray [4,-1,2,1]).

