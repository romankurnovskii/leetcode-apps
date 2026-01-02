## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of integers and a target n, we need to count the number of pairs (i, j) where i < j, both elements are non-zero, and their sum equals n.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n^2) - we check all pairs, where n is the array length.
- **Space Complexity:** O(1) - we only need variables for counting.
- **Edge Case:** If the array has fewer than 2 elements, return 0. If no pairs sum to n, return 0.

**1.2 High-level approach:**

The goal is to check all pairs of elements and count those where both are non-zero and sum to n.

![Pair counting visualization](https://assets.leetcode.com/static_assets/others/pair-count.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all pairs. This is O(n^2) which is acceptable for the constraints.
- **Optimized Strategy:** We could use a hash set to find complements, but for clarity, we check all pairs.
- **Optimization:** The O(n^2) approach is straightforward and works for the given constraints.

**1.4 Decomposition:**

1. For each element at index i:
   - For each element at index j > i:
     - Check if nums[i] != 0 and nums[j] != 0.
     - Check if nums[i] + nums[j] == n.
     - If both conditions true, increment count.
2. Return the count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 0, 3, 4]`, `n = 5`

- Array: `[1, 2, 0, 3, 4]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We check all pairs.

**2.3 Trace Walkthrough:**

| Step | i | j | nums[i] | nums[j] | Non-zero? | Sum == 5? | res |
| ---- | - | - | ------- | ------- | --------- | --------- | --- |
| 1    | 0 | 1 | 1 | 2 | Yes | No (3) | 0 |
| 2    | 0 | 3 | 1 | 3 | Yes | No (4) | 0 |
| 3    | 0 | 4 | 1 | 4 | Yes | Yes | 1 |
| 4    | 1 | 3 | 2 | 3 | Yes | Yes | 2 |
| 5    | 1 | 4 | 2 | 4 | Yes | No (6) | 2 |

**2.4 Increment and Loop:**

After checking each pair, we update the count.

**2.5 Return Result:**

The result is `2`, which is the number of pairs that sum to 5: (1,4) and (2,3).

