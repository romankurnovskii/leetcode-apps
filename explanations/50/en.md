# Problem 50: Pow(x, n)
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/powx-n/

## Explanation

### Strategy (The "Why")

The problem asks us to calculate $x$ raised to the power $n$ (i.e., $x^n$), where $x$ is a floating-point number and $n$ is an integer that can be positive, negative, or zero.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $x$ can be any floating-point number in the range $(-100.0, 100.0)$, and $n$ can be any integer in the range $[-2^{31}, 2^{31}-1]$.
- **Time Complexity:** $O(\log n)$ - We use exponentiation by squaring, which reduces the number of multiplications from $n$ to approximately $\log_2 n$ by repeatedly halving the exponent.
- **Space Complexity:** $O(\log n)$ - The recursive call stack depth is proportional to $\log n$ since we divide the exponent in half at each step.
- **Edge Case:** When $n$ is negative, we convert it to a positive exponent by taking the reciprocal of $x$ (i.e., $x^{-n} = (1/x)^n$).

**1.2 High-level approach:**

The goal is to compute $x^n$ efficiently without performing $n$ multiplications. We use the mathematical property that $x^n = (x^{n/2})^2$ when $n$ is even, and $x^n = x \cdot (x^{n/2})^2$ when $n$ is odd. This allows us to reduce the problem size by half at each step.

![Exponentiation by squaring visualization](https://assets.leetcode.com/static_assets/others/pow-recursion-tree.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Multiply $x$ by itself $n$ times. This requires $O(n)$ time and $O(1)$ space, which is inefficient for large values of $n$ (e.g., $n = 2^{31}$ would require billions of operations).
- **Optimized (Exponentiation by Squaring):** Recursively compute $x^{n/2}$ and square the result, handling odd exponents by multiplying by $x$ once. This reduces time complexity to $O(\log n)$ and space to $O(\log n)$ for the recursion stack.
- **Emphasize the optimization:** By halving the exponent at each step, we transform a linear problem into a logarithmic one, making it feasible to compute even very large powers efficiently.

**1.4 Decomposition:**

1. **Handle Negative Exponent:** If $n$ is negative, convert the problem to computing $(1/x)^{-n}$ by inverting $x$ and making $n$ positive.
2. **Base Case:** If $n$ is zero, return $1.0$ (any number raised to the power of zero equals one).
3. **Recursive Calculation:** Compute $x^{n/2}$ recursively, storing the result.
4. **Combine Results:** If $n$ is even, return the square of the recursive result. If $n$ is odd, multiply the recursive result squared by $x$ once.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: $x = 2.0$, $n = 10$.

We want to compute $2^{10} = 1024$.

**2.2 Start Processing:**

The function first checks if $n < 0$. In our example, $n = 10$ is positive, so we proceed with $x = 2.0$ and $n = 10$.

**2.3 Trace Walkthrough:**

The recursive calls proceed as follows:

| Recursive Call | $n$ | $n$ % 2 | Calculation | Result |
|----------------|-----|---------|-------------|--------|
| `myPow(2.0, 10)` | 10 | 0 (even) | `res = myPow(2.0, 5)` → $32^2 = 1024$ | 1024 |
| `myPow(2.0, 5)` | 5 | 1 (odd) | `res = myPow(2.0, 2)` → $2 \times 4^2 = 32$ | 32 |
| `myPow(2.0, 2)` | 2 | 0 (even) | `res = myPow(2.0, 1)` → $2^2 = 4$ | 4 |
| `myPow(2.0, 1)` | 1 | 1 (odd) | `res = myPow(2.0, 0)` → $2 \times 1^2 = 2$ | 2 |
| `myPow(2.0, 0)` | 0 | - | Base case: return $1.0$ | 1 |

**2.4 Recursive Unwinding:**

Starting from the base case:
- `myPow(2.0, 0)` returns $1$
- `myPow(2.0, 1)` computes $2 \times 1^2 = 2$
- `myPow(2.0, 2)` computes $2^2 = 4$
- `myPow(2.0, 5)` computes $2 \times 4^2 = 2 \times 16 = 32$
- `myPow(2.0, 10)` computes $32^2 = 1024$

**2.5 Return Result:**

The final result is $1024$, which is $2^{10}$.

> **Note:** For negative exponents, the algorithm first converts $x^{-n}$ to $(1/x)^n$. For example, $2^{-2}$ becomes $(1/2)^2 = 0.25$.

