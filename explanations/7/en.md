## Explanation

### Strategy (The "Why")

Given a signed 32-bit integer `x`, we need to return `x` with its digits reversed. If reversing causes the value to go outside the 32-bit signed integer range $[-2^{31}, 2^{31} - 1]$, return 0.

**1.1 Constraints & Complexity:**

- **Input Size:** $x$ is a 32-bit integer.
- **Value Range:** $x$ is between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(\log_{10}(x))$ - We process each digit once. The number of digits is logarithmic in the value.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If $x = 0$, return 0. If reversing causes overflow, return 0.

**1.2 High-level approach:**

The goal is to reverse the digits of an integer while handling overflow.

We extract digits from right to left, build the reversed number, and check for overflow before returning. We handle the sign separately.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert to string, reverse, convert back. This works but is less efficient.
- **Optimized Strategy (Mathematical):** Extract digits mathematically using modulo and division. This is more efficient and handles overflow naturally.
- **Why it's better:** The mathematical approach is more efficient and allows us to check for overflow during the reversal process, avoiding the need for string conversion.

**1.4 Decomposition:**

1. Store the sign of the number.
2. Work with the absolute value.
3. Extract digits from right to left using modulo and division.
4. Build the reversed number digit by digit.
5. Check if the result is within 32-bit integer bounds.
6. Return the result with the original sign applied.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $x = 123$

We initialize:
- `sign = 1` (positive)
- `x = 123` (absolute value)
- `reversed_num = 0`

**2.2 Start Reversing:**

We begin extracting digits.

**2.3 Trace Walkthrough:**

| Step | x | x % 10 | reversed_num Before | reversed_num After | x After |
|------|---|--------|---------------------|-------------------|---------|
| 1 | 123 | 3 | 0 | $0 \times 10 + 3 = 3$ | 12 |
| 2 | 12 | 2 | 3 | $3 \times 10 + 2 = 32$ | 1 |
| 3 | 1 | 1 | 32 | $32 \times 10 + 1 = 321$ | 0 |

**2.4 Check Overflow:**

- Result = 321
- Check: $-2^{31} \leq 321 \leq 2^{31} - 1$ ✓
- Apply sign: $1 \times 321 = 321$

**2.5 Return Result:**

We return 321, which is the reversed number.

> **Note:** The key is to extract digits from right to left using `x % 10` and build the reversed number by multiplying by 10 and adding the digit. We check for overflow after building the number.

