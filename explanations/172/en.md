## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $0 \leq n \leq 10^4$.
- **Time Complexity:** $O(\log n)$ where $n$ is the input number. We divide by 5 repeatedly.
- **Space Complexity:** $O(1)$ as we only use a constant amount of extra space.
- **Edge Case:** If $n = 0$ or $n < 5$, return 0 (no trailing zeroes).

**1.2 High-level approach:**

The goal is to count the number of trailing zeroes in $n!$. Trailing zeroes are created by factors of 10, which come from pairs of 2 and 5. Since there are always more factors of 2 than 5, we only need to count factors of 5. We count 5, 25, 125, etc., as each contributes to trailing zeroes.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate $n!$ and count trailing zeroes. This is impractical for large $n$ due to overflow and inefficiency.
- **Optimized Strategy:** Count factors of 5 by repeatedly dividing $n$ by 5. This is $O(\log n)$ time.
- **Why optimized is better:** The optimized approach avoids calculating the factorial and directly counts the relevant factors, making it efficient even for large $n$.

**1.4 Decomposition:**

1. Initialize `res = 0`.
2. While $n > 0$:
   - Divide $n$ by 5: $n = n // 5$
   - Add the quotient to `res`.
3. Return `res`.

This counts:
- Numbers divisible by 5: $n // 5$
- Numbers divisible by 25: $n // 25$ (each contributes an extra 5)
- Numbers divisible by 125: $n // 125$ (each contributes another extra 5)
- And so on...

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 25`

We initialize `res = 0`.

**2.2 Start Checking:**

We repeatedly divide $n$ by 5 and add the quotient to `res`.

**2.3 Trace Walkthrough:**

| Iteration | n | n // 5 | res before | res after |
|-----------|---|--------|------------|-----------|
| 1 | 25 | 5 | 0 | 5 |
| 2 | 5 | 1 | 5 | 6 |
| 3 | 1 | 0 | 6 | 6 |
| 4 | 0 | - | 6 | 6 (stop) |

**Explanation:**
- First iteration: Count numbers divisible by 5: 5, 10, 15, 20, 25 → 5 numbers
- Second iteration: Count numbers divisible by 25: 25 → 1 number (25 contributes an extra 5)
- Total: 5 + 1 = 6 trailing zeroes

**2.4 Increment and Loop:**

The loop continues while $n > 0$:
- `n //= 5`: Divide $n$ by 5 (integer division)
- `res += n`: Add the quotient to the result

**2.5 Return Result:**

For $n = 25$, we get `res = 6`. This means $25!$ has 6 trailing zeroes. We return `6`.

**Verification:** $25! = 15511210043330985984000000$ has 6 trailing zeroes, confirming our result.

