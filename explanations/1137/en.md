## Explanation

### Strategy (The "Why")

Given an integer `n`, we need to return the $n$-th Tribonacci number. The Tribonacci sequence is defined as: $T(0) = 0$, $T(1) = 1$, $T(2) = 1$, and $T(n) = T(n-1) + T(n-2) + T(n-3)$ for $n \geq 3$.

**1.1 Constraints & Complexity:**

- **Input Size:** $n$ can be between $0$ and $37$.
- **Value Range:** Tribonacci numbers grow exponentially, but $n$ is small enough that results fit in standard integers.
- **Time Complexity:** $O(n)$ - We iterate from 3 to $n$ once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables.
- **Edge Case:** If $n = 0$, return 0. If $n = 1$ or $n = 2$, return 1.

**1.2 High-level approach:**

The goal is to compute the $n$-th Tribonacci number efficiently.

We use an iterative approach (bottom-up dynamic programming) instead of recursion. We maintain the last three Tribonacci numbers and compute the next one iteratively.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force (Recursion):** Recursively compute $T(n) = T(n-1) + T(n-2) + T(n-3)$. This takes exponential time due to repeated calculations.
- **Optimized Strategy (Iterative DP):** Use iteration to build up Tribonacci numbers from bottom to top. This takes $O(n)$ time.
- **Why it's better:** The iterative approach reduces time complexity from exponential to linear by computing each Tribonacci number only once, avoiding redundant recursive calls.

**1.4 Decomposition:**

1. Handle base cases: if $n = 0$, return 0; if $n \leq 2$, return 1.
2. Initialize `prev3 = 0` (T(0)), `prev2 = 1` (T(1)), `prev1 = 1` (T(2)).
3. Iterate from 3 to $n$:
   - Compute current Tribonacci number: `current = prev1 + prev2 + prev3`.
   - Update: `prev3 = prev2`, `prev2 = prev1`, `prev1 = current`.
4. Return `prev1` (which is T(n)).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $n = 4$

We initialize:
- `prev3 = 0` (T(0))
- `prev2 = 1` (T(1))
- `prev1 = 1` (T(2))

**2.2 Start Computing:**

We begin iterating from 3 to 4.

**2.3 Trace Walkthrough:**

| i | prev3 | prev2 | prev1 | current = prev1 + prev2 + prev3 | prev3 After | prev2 After | prev1 After |
|---|-------|-------|-------|--------------------------------|-------------|-------------|-------------|
| 3 | 0 | 1 | 1 | $1 + 1 + 0 = 2$ | 1 | 1 | 2 |
| 4 | 1 | 1 | 2 | $2 + 1 + 1 = 4$ | 1 | 2 | 4 |

**2.4 Final Result:**

After iteration, `prev1 = 4`, which is T(4).

**2.5 Return Result:**

We return 4, which is the 4th Tribonacci number.

> **Note:** The key insight is that we only need the last three Tribonacci numbers to compute the next one. By maintaining just three variables and updating them iteratively, we avoid the exponential time complexity of naive recursion.

