## Explanation

### Strategy (The "Why")

Given an integer `n`, we need to calculate the $n$-th Fibonacci number. The Fibonacci sequence is defined as: $F(0) = 0$, $F(1) = 1$, and $F(n) = F(n-1) + F(n-2)$ for $n > 1$.

**1.1 Constraints & Complexity:**

- **Input Size:** $n$ can be between $0$ and $30$.
- **Value Range:** Fibonacci numbers grow exponentially, but $n$ is small enough that results fit in standard integers.
- **Time Complexity:** $O(n)$ - We iterate from 2 to $n$ once.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space for variables.
- **Edge Case:** If $n = 0$, return 0. If $n = 1$, return 1.

**1.2 High-level approach:**

The goal is to compute the $n$-th Fibonacci number efficiently.

We use an iterative approach (bottom-up dynamic programming) instead of recursion. We maintain the last two Fibonacci numbers and compute the next one iteratively.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force (Recursion):** Recursively compute $F(n) = F(n-1) + F(n-2)$. This takes $O(2^n)$ time due to repeated calculations.
- **Optimized Strategy (Iterative DP):** Use iteration to build up Fibonacci numbers from bottom to top. This takes $O(n)$ time.
- **Why it's better:** The iterative approach reduces time complexity from exponential to linear by computing each Fibonacci number only once, avoiding redundant recursive calls.

**1.4 Decomposition:**

1. Handle base cases: if $n \leq 1$, return $n$.
2. Initialize `prev2 = 0` (F(0)) and `prev1 = 1` (F(1)).
3. Iterate from 2 to $n$:
   - Compute current Fibonacci number: `current = prev1 + prev2`.
   - Update `prev2 = prev1` and `prev1 = current`.
4. Return `prev1` (which is F(n)).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $n = 5$

We initialize:
- `prev2 = 0` (F(0))
- `prev1 = 1` (F(1))

**2.2 Start Computing:**

We begin iterating from 2 to 5.

**2.3 Trace Walkthrough:**

| i | prev2 | prev1 | current = prev1 + prev2 | prev2 After | prev1 After |
|---|-------|-------|------------------------|-------------|-------------|
| 2 | 0 | 1 | $1 + 0 = 1$ | 1 | 1 |
| 3 | 1 | 1 | $1 + 1 = 2$ | 1 | 2 |
| 4 | 1 | 2 | $2 + 1 = 3$ | 2 | 3 |
| 5 | 2 | 3 | $3 + 2 = 5$ | 3 | 5 |

**2.4 Final Result:**

After iteration, `prev1 = 5`, which is F(5).

**2.5 Return Result:**

We return 5, which is the 5th Fibonacci number.

> **Note:** The key insight is that we only need the last two Fibonacci numbers to compute the next one. By maintaining just two variables and updating them iteratively, we avoid the exponential time complexity of naive recursion.

