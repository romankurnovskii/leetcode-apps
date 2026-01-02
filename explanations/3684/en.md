## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array and an integer k, we need to find the maximum sum of at most k distinct elements.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n log n) - we need to sort elements by value, where n is the array length.
- **Space Complexity:** O(n) - we need to store frequency counts and distinct elements.
- **Edge Case:** If k is 0, return 0. If k >= number of distinct elements, return sum of all distinct elements.

**1.2 High-level approach:**

The goal is to select the k largest distinct elements and sum them.

![Distinct elements sum visualization](https://assets.leetcode.com/static_assets/others/distinct-sum.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all combinations of distinct elements. This is exponential.
- **Optimized Strategy:** Count frequencies, get distinct elements, sort in descending order, take top k. This is O(n log n) time.
- **Optimization:** By sorting and taking top k, we efficiently find the maximum sum.

**1.4 Decomposition:**

1. Count frequency of each element.
2. Get list of distinct elements.
3. Sort distinct elements in descending order.
4. Sum the top k elements (or all if fewer than k).
5. Return the sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1, 2, 2, 3, 3, 3]`, `k = 2`

- Distinct elements: `[1, 2, 3]`
- Sorted: `[3, 2, 1]`
- Result variable: `res = 0`

**2.2 Start Checking:**

We take the top k distinct elements.

**2.3 Trace Walkthrough:**

| Step | Element | Add to sum | res |
| ---- | ------- | ---------- | --- |
| 1    | 3 | Yes (top 1) | 3 |
| 2    | 2 | Yes (top 2) | 5 |
| 3    | 1 | No (k=2) | 5 |

**2.4 Increment and Loop:**

After processing each element, we check if we've reached k elements.

**2.5 Return Result:**

The result is `5`, which is the sum of the top 2 distinct elements (3 + 2).

