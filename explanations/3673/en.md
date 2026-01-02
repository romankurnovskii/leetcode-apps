## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array, we need to find the sum of (value × frequency) for all elements that have the maximum frequency (mode).

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n) - we count frequencies once, where n is the array length.
- **Space Complexity:** O(n) - we need to store frequency counts.
- **Edge Case:** If the array is empty, return 0. If all elements have the same frequency, sum all (value × frequency).

**1.2 High-level approach:**

The goal is to find the maximum frequency, then sum (value × frequency) for all elements with that frequency.

![Weighted mode visualization](https://assets.leetcode.com/static_assets/others/weighted-mode.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** This problem is straightforward - count frequencies and find maximum.
- **Optimized Strategy:** Count frequencies, find maximum frequency, then sum weighted values. This is O(n) time.
- **Optimization:** The solution is already optimal - linear time.

**1.4 Decomposition:**

1. Count frequency of each element.
2. Find the maximum frequency.
3. For each element with maximum frequency, add (value × frequency) to sum.
4. Return the sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 2, 3, 3, 3]`

- Frequency counts: `{1: 1, 2: 2, 3: 3}`
- Maximum frequency: `3`
- Result variable: `res = 0`

**2.2 Start Checking:**

We sum weighted values for elements with max frequency.

**2.3 Trace Walkthrough:**

| Step | Element | Frequency | Is max? | Add to sum | res |
| ---- | ------- | --------- | ------- | ---------- | --- |
| 1    | 1 | 1 | No | 0 | 0 |
| 2    | 2 | 2 | No | 0 | 0 |
| 3    | 3 | 3 | Yes | 3×3=9 | 9 |

**2.4 Increment and Loop:**

After processing each element, we add to sum if it has max frequency.

**2.5 Return Result:**

The result is `9`, which is the sum of (value × frequency) for the mode element 3 (3 × 3 = 9).

