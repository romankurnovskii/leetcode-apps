## Explanation

### Strategy (The "Why")

Given a signed 32-bit integer `x`, we need to reverse its digits. If reversing causes overflow, return 0.

**1.1 Constraints & Complexity:**

- **Input Size:** $x$ is a 32-bit integer, so between $-2^{31}$ and $2^{31} - 1$.
- **Value Range:** Input can be between $-2^{31}$ and $2^{31} - 1$.
- **Time Complexity:** $O(\log_{10}(x))$ - We process each digit once. The number of digits is $\log_{10}(x)$.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If $x = 0$, return 0. If reversing causes overflow (result outside 32-bit range), return 0.

**1.2 High-level approach:**

The goal is to reverse the digits of an integer while handling overflow.

We extract digits from right to left, build the reversed number, and check for overflow before returning.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert to string, reverse, convert back. This works but is less efficient.
- **Optimized Strategy (Math):** Extract digits using modulo and division, build reversed number mathematically. This is more efficient and handles overflow naturally.
- **Why it's better:** The mathematical approach is more efficient and allows us to check for overflow before it happens by checking the bounds.

**1.4 Decomposition:**

1. Store the sign of the number.
2. Work with the absolute value.
3. Extract digits from right to left using modulo and division.
4. Build the reversed number digit by digit.
5. Apply the sign.
6. Check for 32-bit integer overflow and return 0 if overflow occurs.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $x = 123$

We initialize:
- `sign = 1` (positive)
- `x = 123`
- `reversed_num = 0`

**2.2 Start Reversing:**

We begin extracting digits.

**2.3 Trace Walkthrough:**

| Step | x | x % 10 | reversed_num Before | reversed_num After | x After |
|------|---|--------|---------------------|-------------------|---------|
| 1 | 123 | 3 | 0 | $0 \times 10 + 3 = 3$ | 12 |
| 2 | 12 | 2 | 3 | $3 \times 10 + 2 = 32$ | 1 |
| 3 | 1 | 1 | 32 | $32 \times 10 + 1 = 321$ | 0 |

**2.4 Apply Sign and Check Overflow:**

- `reversed_num = 321`
- Apply sign: $321 \times 1 = 321$
- Check overflow: $321$ is within $[-2^{31}, 2^{31}-1] = [-2147483648, 2147483647]$ ✓

**2.5 Return Result:**

We return 321, which is the reversed integer.

> **Note:** The key is to extract digits from right to left using modulo and division, then build the reversed number. We check for overflow by comparing with 32-bit integer bounds before returning.

