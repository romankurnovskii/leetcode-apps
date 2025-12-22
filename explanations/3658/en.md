## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to compute the GCD (greatest common divisor) of two values: the sum of the first n odd numbers and the sum of the first n even numbers.

**1.1 Constraints & Complexity:**

- **Input Size:** n can be up to 1000.
- **Time Complexity:** O(1) - we use a mathematical formula to compute the answer directly without iterating.
- **Space Complexity:** O(1) - we only use a constant amount of space.
- **Edge Case:** For n = 1, sumOdd = 1, sumEven = 2, GCD(1, 2) = 1.

**1.2 High-level approach:**

The goal is to find a mathematical relationship between the sums of odd and even numbers, then compute their GCD efficiently. The key insight is that we can express both sums in terms of n, which allows us to simplify the GCD calculation.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Calculate both sums explicitly (1+3+5+... and 2+4+6+...), then compute GCD using Euclidean algorithm. This is O(n) time.
- **Optimized Strategy:** Use mathematical formulas: sum of first n odd numbers = n², sum of first n even numbers = n(n+1). Then GCD(n², n(n+1)) = n × GCD(n, n+1) = n × 1 = n. This is O(1) time.
- **Optimization:** By recognizing the mathematical patterns, we avoid computing the sums explicitly and can derive the answer directly.

**1.4 Decomposition:**

1. Recognize that the sum of first n odd numbers equals n².
2. Recognize that the sum of first n even numbers equals n(n+1).
3. Apply GCD property: GCD(n², n(n+1)) = n × GCD(n, n+1).
4. Use the fact that consecutive integers are coprime: GCD(n, n+1) = 1.
5. Conclude that the answer is n.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 4`

- We need to find GCD(sumOdd, sumEven) where:
  - sumOdd = 1 + 3 + 5 + 7 = 16
  - sumEven = 2 + 4 + 6 + 8 = 20

**2.2 Start Processing:**

We apply the mathematical formulas to express the sums in terms of n.

**2.3 Trace Walkthrough:**

| Step | Calculation | Result |
|------|-------------|--------|
| 1 | sumOdd = n² = 4² | 16 |
| 2 | sumEven = n(n+1) = 4×5 | 20 |
| 3 | GCD(16, 20) = GCD(4², 4×5) | - |
| 4 | = 4 × GCD(4, 5) | - |
| 5 | = 4 × 1 (since 4 and 5 are consecutive) | 4 |

For `n = 5`:
- sumOdd = 5² = 25
- sumEven = 5×6 = 30
- GCD(25, 30) = GCD(5², 5×6) = 5 × GCD(5, 6) = 5 × 1 = 5

**2.4 Increment and Loop:**

The algorithm is a direct calculation with no loops needed.

**2.5 Return Result:**

For `n = 4`, the result is 4. The GCD of the sum of first 4 odd numbers (16) and first 4 even numbers (20) is 4.

For `n = 5`, the result is 5. The GCD of the sum of first 5 odd numbers (25) and first 5 even numbers (30) is 5.

