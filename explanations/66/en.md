## Explanation

### Strategy (The "Why")

Given a non-empty array of digits representing a non-negative integer, we need to increment the integer by one and return the resulting array of digits.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $1$ and $100$.
- **Value Range:** Each digit is between $0$ and $9$.
- **Time Complexity:** $O(n)$ - In the worst case, we iterate through all digits once.
- **Space Complexity:** $O(1)$ - We modify the input array in-place. Only in the case where all digits are 9, we create a new array of size $n+1$.
- **Edge Case:** If all digits are 9, we need to add a new digit 1 at the beginning (e.g., $[9,9] \rightarrow [1,0,0]$).

**1.2 High-level approach:**

The goal is to add 1 to a number represented as an array of digits.

![Plus One](https://assets.leetcode.com/uploads/2021/04/21/plusone-diagram.jpg)

We work from right to left, handling carry-over. If a digit is less than 9, we increment it and return. If it's 9, we set it to 0 and continue. If all digits are 9, we add 1 at the beginning.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Convert the array to an integer, add 1, then convert back to an array. This might overflow for large numbers.
- **Optimized Strategy (In-place):** Work from right to left, handling carry-over directly in the array. This avoids conversion and handles large numbers.
- **Why it's better:** The in-place approach avoids potential integer overflow and is more efficient, working directly with the digit array.

**1.4 Decomposition:**

1. Start from the rightmost digit (ones place).
2. If the digit is less than 9, increment it and return the array.
3. If the digit is 9, set it to 0 and move to the next digit to the left (carry over).
4. Continue until we find a digit less than 9 or reach the beginning.
5. If all digits were 9, return a new array with 1 followed by zeros.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $digits = [1,2,3]$

We start from index 2 (rightmost digit).

**2.2 Start Processing:**

We check each digit from right to left.

**2.3 Trace Walkthrough:**

**Example 1:** $digits = [1,2,3]$
- Index 2: $3 < 9$ → increment to 4 → return $[1,2,4]$

**Example 2:** $digits = [1,2,9]$
- Index 2: $9$ → set to 0, continue
- Index 1: $2 < 9$ → increment to 3 → return $[1,3,0]$

**Example 3:** $digits = [9,9,9]$
- Index 2: $9$ → set to 0, continue
- Index 1: $9$ → set to 0, continue
- Index 0: $9$ → set to 0, continue
- All digits were 9 → return $[1,0,0,0]$

**2.4 Detailed Trace for [9,9,9]:**

| Step | Index | Digit | Action | Array State |
|------|-------|-------|--------|-------------|
| 1 | 2 | 9 | Set to 0 | $[9,9,0]$ |
| 2 | 1 | 9 | Set to 0 | $[9,0,0]$ |
| 3 | 0 | 9 | Set to 0 | $[0,0,0]$ |
| 4 | - | - | All 9s | Return $[1,0,0,0]$ |

**2.5 Return Result:**

- For $[1,2,3]$: return $[1,2,4]$
- For $[9,9,9]$: return $[1,0,0,0]$

> **Note:** The key insight is that we only need to modify digits when there's a carry-over. Once we find a digit less than 9, we can increment it and return immediately, as no further carry-over is needed.
