## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `n == nums.length` where `1 <= n <= 10^5`.
- **Value Range:** Each `nums[i]` is in the range `[1, n]`.
- **Time Complexity:** O(n) - we make two passes through the array.
- **Space Complexity:** O(1) - we reuse the input array for marking, and the result array doesn't count as extra space per the problem statement.
- **Edge Case:** If all numbers from 1 to n appear, return an empty list.

**1.2 High-level approach:**

The goal is to find all numbers in the range `[1, n]` that do not appear in the input array. The key insight is that we can use the array itself to mark which numbers have appeared by negating values at specific indices. Since numbers are in the range `[1, n]`, we can use `nums[i] - 1` as an index to mark that the number `nums[i]` has appeared.

![Visualization showing how we mark numbers by negating values at their corresponding indices]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Use a set or hash map to track all numbers that appear, then iterate through 1 to n to find missing numbers. This requires O(n) extra space.
- **Optimized Strategy:** Use the input array itself as a marker by negating values. This requires no extra space beyond the result array.
- **Why it's better:** The optimized approach uses O(1) extra space by cleverly reusing the input array, which is important for large inputs.

**1.4 Decomposition:**

1. First pass: For each number in the array, mark its presence by negating the value at index `abs(num) - 1`.
2. Second pass: Collect all indices where the value is still positive - these correspond to missing numbers.
3. Return the list of missing numbers (indices + 1).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [4, 3, 2, 7, 8, 2, 3, 1]`.

We need to find numbers from 1 to 8 that are missing. The array has length 8.

**2.2 Start Checking:**

First pass: Mark numbers that appear by negating values at their corresponding indices.

**2.3 Trace Walkthrough:**

| Step | num | idx = abs(num) - 1 | nums[idx] before | nums[idx] after | nums array state |
|------|-----|---------------------|------------------|-----------------|------------------|
| 1 | 4 | 3 | 7 | -7 | [4, 3, 2, -7, 8, 2, 3, 1] |
| 2 | 3 | 2 | 2 | -2 | [4, 3, -2, -7, 8, 2, 3, 1] |
| 3 | 2 | 1 | 3 | -3 | [4, -3, -2, -7, 8, 2, 3, 1] |
| 4 | 7 | 6 | 3 | -3 | [4, -3, -2, -7, 8, 2, -3, 1] |
| 5 | 8 | 7 | 1 | -1 | [4, -3, -2, -7, 8, 2, -3, -1] |
| 6 | 2 | 1 | -3 | -3 | [4, -3, -2, -7, 8, 2, -3, -1] |
| 7 | 3 | 2 | -2 | -2 | [4, -3, -2, -7, 8, 2, -3, -1] |
| 8 | 1 | 0 | 4 | -4 | [-4, -3, -2, -7, 8, 2, -3, -1] |

**2.4 Increment and Loop:**

Second pass: Check which indices have positive values (these are missing numbers).

| Index i | nums[i] | Is positive? | Missing number (i + 1) |
|--------|---------|--------------|------------------------|
| 0 | -4 | No | - |
| 1 | -3 | No | - |
| 2 | -2 | No | - |
| 3 | -7 | No | - |
| 4 | 8 | Yes | 5 |
| 5 | 2 | Yes | 6 |
| 6 | -3 | No | - |
| 7 | -1 | No | - |

**2.5 Return Result:**

Return `res = [5, 6]` - these are the numbers missing from the array.

