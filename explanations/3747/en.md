## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 10^{15}$.
- **Time Complexity:** $O(d)$ where $d$ is the number of digits in $n$ (at most 16 digits).
- **Space Complexity:** $O(d)$ for storing the string representation and power array.
- **Edge Case:** If $n = 1$, return 1. If $n$ contains a zero, we stop counting at that position.

**1.2 High-level approach:**

The goal is to count distinct integers from $[1, n]$ after removing all zeros from their decimal representation. Key insight: numbers with zeros, when zeros are removed, produce numbers that were already counted. So we need to count only numbers that don't contain any zeros.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Generate all numbers from 1 to $n$, remove zeros, and count distinct values. This is infeasible for $n = 10^{15}$.
- **Optimized Strategy:** Count numbers without zeros using combinatorics. For each digit position, we can place digits 1-9 (9 choices). Use digit DP or combinatorial counting. This is $O(d)$ time.
- **Why optimized is better:** The combinatorial approach avoids generating all numbers and works efficiently even for very large $n$.

**1.4 Decomposition:**

1. Convert $n$ to string for digit-by-digit processing.
2. Precompute powers of 9 (for digits 1-9, excluding 0).
3. Count all numbers with fewer digits than $n$: sum of $9^l$ for $l = 1$ to $len(n)-1$.
4. Count numbers with same number of digits as $n$ but $\leq n$: for each digit position, count valid numbers.
5. If $n$ itself has no zeros, add 1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 273`

We convert to string: `s = "273"`, length = 3.

**2.2 Start Checking:**

We count numbers with 1 and 2 digits, then count 3-digit numbers $\leq 273$.

**2.3 Trace Walkthrough:**

| Step | Action | Count |
|------|--------|-------|
| 1 | Count 1-digit numbers (1-9) | $9^1 = 9$ |
| 2 | Count 2-digit numbers (10-99, no zeros) | $9^2 = 81$ |
| 3 | Count 3-digit numbers starting with 1 | $(1-1) \times 9^2 = 0$ |
| 4 | Count 3-digit numbers starting with 2, second digit 1-6 | $(2-1) \times 9^1 = 9$ (for second digit 1-6: 6 cases) |
| 5 | For "27X", third digit 1-2 | $(7-1) \times 9^0 = 6$ |
| 6 | Check if 273 has no zeros | Yes, add 1 |
| Total | | $9 + 81 + 0 + 9 + 6 + 1 = 106$ |

**2.4 Increment and Loop:**

- Precompute: `pow9[i] = 9^i` for $i = 0$ to $len(s)$
- Count shorter numbers: `for l in range(1, len(s)): res += pow9[l]`
- Count same-length numbers: for each digit position $i$:
  - If digit is 0, break (can't form more valid numbers)
  - For each digit $d$ from 1 to $(digit-1)$: `res += pow9[len(s) - i - 1]`

**2.5 Return Result:**

For $n = 273$, we count all numbers from 1 to 273 that don't contain zeros. The result is the number of distinct integers after removing zeros from all numbers in $[1, 273]$.

