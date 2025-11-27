## Explanation

### Strategy (The "Why")

Given an array of non-negative integers `nums` and a target integer `target`, we need to find the number of ways to assign `+` or `-` signs to each number such that the sum equals the target.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $20$.
- **Value Range:** Each number is between $0$ and $1000$, and the sum of all numbers is at most $1000$.
- **Time Complexity:** $O(n \times sum)$ - With memoization, we compute each $(index, sum)$ pair at most once. The number of unique states is $n \times (2 \times sum + 1)$.
- **Space Complexity:** $O(n \times sum)$ - The memoization dictionary stores at most $n \times (2 \times sum + 1)$ entries. The recursion stack depth is $O(n)$.
- **Edge Case:** If the target is greater than the sum of all numbers, there's no solution (return 0). If target is 0 and all numbers are 0, there are $2^n$ ways.

**1.2 High-level approach:**

The goal is to count the number of ways to assign signs to numbers to reach the target sum.

![Target Sum](https://assets.leetcode.com/uploads/2021/04/09/targetsum.jpg)

We use recursion with memoization. At each number, we try both adding it and subtracting it, then recursively solve for the remaining numbers and updated target.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all $2^n$ possible sign assignments, calculate the sum for each, and count how many equal the target. This takes $O(2^n)$ time.
- **Optimized Strategy (Memoization):** Use recursion with memoization to avoid recalculating the same subproblems. We memoize results for $(index, current\_sum)$ pairs.
- **Why it's better:** Memoization reduces the time complexity from exponential to polynomial. Many sign assignments lead to the same intermediate sums, and we only compute each unique state once.

**1.4 Decomposition:**

1. Use a recursive function that takes the current index and current sum.
2. Base case: if we've processed all numbers, return 1 if the sum equals target, else 0.
3. For each number, try both adding it and subtracting it.
4. Memoize results to avoid recalculating the same $(index, sum)$ states.
5. Return the sum of ways from both choices (add and subtract).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [1, 1, 1, 1, 1]$, $target = 3$

We initialize:
- `memo = {}` (empty memoization dictionary)
- Start with `index = 0`, `current_sum = 0`

**2.2 Start Recursion:**

We begin the recursive exploration from index 0.

**2.3 Trace Walkthrough:**

The recursion tree (simplified, showing key paths):

| Index | Current Sum | Choice | New Sum | Continue? |
|-------|-------------|--------|---------|------------|
| 0 | 0 | +1 | 1 | Yes |
| 1 | 1 | +1 | 2 | Yes |
| 2 | 2 | +1 | 3 | Yes |
| 3 | 3 | +1 | 4 | Yes |
| 4 | 4 | +1 | 5 | Base: $5 \neq 3$ → 0 |
| 4 | 4 | -1 | 3 | Base: $3 == 3$ → 1 |

One valid path: $+1 +1 +1 +1 -1 = 3$

**2.4 Memoization Benefits:**

Without memoization, we'd recalculate the same states many times. For example, reaching sum 2 at index 2 can happen through multiple paths (e.g., $+1+1$ or $+1-1+1+1$), but we only need to compute it once.

**2.5 Return Result:**

The function returns the total count of ways to reach target 3. For this example, there are 5 ways:
- $+1 +1 +1 +1 -1 = 3$
- $+1 +1 +1 -1 +1 = 3$
- $+1 +1 -1 +1 +1 = 3$
- $+1 -1 +1 +1 +1 = 3$
- $-1 +1 +1 +1 +1 = 3$

> **Note:** The memoization is crucial for efficiency. Without it, the solution would be too slow for larger inputs. The key insight is that we only care about the current index and current sum, not the exact path that got us there.

