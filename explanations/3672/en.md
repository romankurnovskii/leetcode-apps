## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to find the sum of (value × frequency) for mode elements across all possible subarrays.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 100 elements.
- **Time Complexity:** O(n^3) - we check all subarrays (O(n^2)) and for each, find mode (O(n)), where n is the array length.
- **Space Complexity:** O(n) - we need to store frequency counts for each subarray.
- **Edge Case:** If the array is empty, return 0. If all elements are the same, all subarrays have the same mode.

**1.2 High-level approach:**

The goal is to check all possible subarrays, find the mode (most frequent element) in each, and sum (mode_value × frequency) for all subarrays.

![Subarray mode visualization](https://assets.leetcode.com/static_assets/others/subarray-mode.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all subarrays and find mode in each. This is O(n^3) which is acceptable for n <= 100.
- **Optimized Strategy:** The current approach is reasonable for the constraints.
- **Optimization:** For larger arrays, we could optimize, but O(n^3) works for the given constraints.

**1.4 Decomposition:**

1. For each starting position i:
   - For each ending position j >= i:
     - Extract subarray nums[i:j+1].
     - Count frequencies in subarray.
     - Find maximum frequency (mode frequency).
     - Sum (value × frequency) for all elements with mode frequency.
     - Add to total.
2. Return the total sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 2]`

- Array: `[1, 2, 2]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We check all possible subarrays.

**2.3 Trace Walkthrough:**

| Step | Subarray | Frequencies | Mode freq | Sum | res |
| ---- | -------- | ----------- | --------- | --- | --- |
| 1    | [1] | {1:1} | 1 | 1×1=1 | 1 |
| 2    | [1,2] | {1:1,2:1} | 1 | 1×1+2×1=3 | 4 |
| 3    | [1,2,2] | {1:1,2:2} | 2 | 2×2=4 | 8 |
| 4    | [2] | {2:1} | 1 | 2×1=2 | 10 |
| 5    | [2,2] | {2:2} | 2 | 2×2=4 | 14 |

**2.4 Increment and Loop:**

After processing each subarray, we add the weighted mode sum to the total.

**2.5 Return Result:**

The result is `14`, which is the sum of weighted modes across all subarrays.

