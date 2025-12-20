## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to split an integer n into exactly k positive integers such that their product equals n, and we want to minimize the maximum difference between any two numbers in the split.

**1.1 Constraints & Complexity:**

- **Input Size:** n can be up to 10^5, and k is between 2 and 5.
- **Time Complexity:** O(d^k) where d is the number of divisors of n - we use backtracking to try all combinations of k divisors. Since k is small (≤5) and the number of divisors is typically small, this is feasible.
- **Space Complexity:** O(d + k) - we store all divisors and the current path during backtracking.
- **Edge Case:** If n is a prime number, the only valid split is [1, 1, ..., 1, n] (k-1 ones and n).

**1.2 High-level approach:**

The goal is to find all divisors of n, then use backtracking to find a combination of k divisors whose product equals n, while minimizing the difference between the maximum and minimum values in the combination.

![Factor decomposition visualization](https://assets.leetcode.com/static_assets/others/factor-decomposition.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of k numbers that multiply to n, which would be exponential and inefficient.
- **Optimized Strategy:** First find all divisors of n, then use backtracking to explore combinations of k divisors. We can prune early when the product exceeds n. This is O(d^k) where d is the number of divisors.
- **Optimization:** By working only with divisors and pruning branches where the product exceeds n, we significantly reduce the search space compared to trying all possible number combinations.

**1.4 Decomposition:**

1. Find all divisors of n by checking numbers from 1 to sqrt(n).
2. Sort the divisors for efficient backtracking.
3. Use backtracking (DFS) to try combinations of k divisors:
   - Start with an empty path and product = 1.
   - For each divisor, try adding it to the path and recursively explore.
   - If we have k divisors and product equals n, check if this combination has a smaller max-min difference.
   - Prune branches where product exceeds n.
4. Return the combination with the minimum max-min difference.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 100`, `k = 2`

- Divisors of 100: [1, 2, 4, 5, 10, 20, 25, 50, 100]
- We need to find 2 divisors whose product is 100 and minimize max - min.

**2.2 Start Processing:**

We begin backtracking with an empty path, product = 1, and picked = 0.

**2.3 Trace Walkthrough:**

| Step | Path | Product | Picked | Action | Valid? |
|------|------|---------|---------|--------|--------|
| 1 | [1] | 1 | 1 | Add divisor 1 | Continue |
| 2 | [1, 1] | 1 | 2 | Add divisor 1 | Product < 100, continue |
| 3 | [1, 100] | 100 | 2 | Add divisor 100 | Product = 100, diff = 99 |
| 4 | [1, 50] | 50 | 2 | Try divisor 50 | Product < 100, backtrack |
| 5 | [10, 10] | 100 | 2 | Try divisor 10 | Product = 100, diff = 0 ✓ |

The best combination is [10, 10] with difference 0.

**2.4 Increment and Loop:**

The backtracking algorithm explores all valid combinations, keeping track of the best result (minimum difference).

**2.5 Return Result:**

The result is [10, 10], which has a product of 100 and a maximum difference of 0, which is the minimum possible.

