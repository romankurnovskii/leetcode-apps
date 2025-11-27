## Explanation

### Strategy (The "Why")

Given an integer array `nums`, we need to determine if there exists a triple of indices $(i, j, k)$ such that $i < j < k$ and $nums[i] < nums[j] < nums[k]$.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be up to $5 \times 10^5$.
- **Value Range:** Array elements are between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(n)$ - We iterate through the array once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for two variables.
- **Edge Case:** If the array has fewer than 3 elements, return false.

**1.2 High-level approach:**

The goal is to find if there exists an increasing triplet subsequence.

![Increasing Triplet](https://assets.leetcode.com/uploads/2020/10/30/increasing-triplet.png)

We maintain two values: `first` (smallest value seen) and `second` (smallest value seen that has a value before it that's smaller). If we find a value greater than both, we've found a triplet.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all triplets, checking if they form an increasing sequence. This takes $O(n^3)$ time.
- **Optimized Strategy (Greedy):** Maintain the two smallest values that could form the start of a triplet. If we find a value greater than both, we've found a triplet. This takes $O(n)$ time.
- **Why it's better:** The greedy approach reduces time complexity from $O(n^3)$ to $O(n)$ by maintaining only the necessary information (two smallest values) instead of checking all triplets.

**1.4 Decomposition:**

1. Initialize `first = \infty` and `second = \infty`.
2. Iterate through each number.
3. If the number is less than or equal to `first`, update `first`.
4. Else if the number is less than or equal to `second`, update `second`.
5. Else (number is greater than both), return true (triplet found).
6. If we finish iterating, return false.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [2,1,5,0,4,6]$

We initialize:
- `first = \infty`
- `second = \infty`

**2.2 Start Processing:**

We iterate through each number.

**2.3 Trace Walkthrough:**

| Number | first | second | Comparison | Action |
|--------|-------|--------|------------|--------|
| 2 | $\infty$ | $\infty$ | $2 \leq \infty$ | `first = 2` |
| 1 | 2 | $\infty$ | $1 \leq 2$ | `first = 1` |
| 5 | 1 | $\infty$ | $5 > 1$ and $5 \leq \infty$ | `second = 5` |
| 0 | 1 | 5 | $0 \leq 1$ | `first = 0` |
| 4 | 0 | 5 | $4 > 0$ and $4 \leq 5$ | `second = 4` |
| 6 | 0 | 4 | $6 > 0$ and $6 > 4$ | **Return True** |

**2.4 Explanation:**

- We found a triplet: `first = 0`, `second = 4`, and `6 > 4 > 0`
- The indices are: $i=3$ (value 0), $j=4$ (value 4), $k=5$ (value 6)

**2.5 Return Result:**

We return `True` because there exists an increasing triplet subsequence.

> **Note:** The key insight is that we don't need to track the exact indices or all possible pairs. We only need to maintain the two smallest values that could form the start of a triplet. If we find a value greater than both, we've found a valid triplet.
