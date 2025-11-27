## Explanation

### Strategy (The "Why")

Given an integer $n$, we need to return an array where each element at index $i$ contains the number of 1's in the binary representation of $i$.

**1.1 Constraints & Complexity:**

- **Input Size:** $n$ can be between $0$ and $10^5$.
- **Value Range:** We're counting bits, so values are between $0$ and the number of bits in $n$.
- **Time Complexity:** $O(n)$ - We iterate through numbers from $1$ to $n$ once.
- **Space Complexity:** $O(n)$ - We create an array of size $n+1$ to store results.
- **Edge Case:** For $n=0$, we return $[0]$ since 0 has zero 1's in binary.

**1.2 High-level approach:**

The goal is to count the number of 1's in the binary representation of each number from 0 to $n$.

![Counting Bits](https://assets.leetcode.com/uploads/2021/03/11/counting-bits.png)

We use dynamic programming with a key insight: the number of 1's in $i$ equals the number of 1's in $i//2$ plus 1 if $i$ is odd (the least significant bit).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each number, convert it to binary and count the 1's. This takes $O(n \log n)$ time because converting to binary takes $O(\log n)$ per number.
- **Optimized Strategy (DP):** Use the relationship that `countBits(i) = countBits(i//2) + (i % 2)`. This allows us to compute each value in $O(1)$ time.
- **Why it's better:** DP reduces the time complexity from $O(n \log n)$ to $O(n)$ by reusing previously computed results instead of recalculating binary representations.

**1.4 Decomposition:**

1. Initialize an array of size $n+1$ with zeros.
2. For each number $i$ from 1 to $n$:
   - The number of 1's in $i$ equals the number of 1's in $i//2$ (right shift by 1) plus 1 if $i$ is odd.
3. Return the array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $n = 5$

We initialize:
- `res = [0, 0, 0, 0, 0, 0]` (for indices 0 to 5)

**2.2 Start Calculating:**

We begin from index 1.

**2.3 Trace Walkthrough:**

| i | Binary | i//2 | res[i//2] | i % 2 | res[i] = res[i//2] + (i % 2) |
|---|--------|------|-----------|-------|------------------------------|
| 0 | 0 | - | - | - | 0 (base case) |
| 1 | 1 | 0 | 0 | 1 | $0 + 1 = 1$ |
| 2 | 10 | 1 | 1 | 0 | $1 + 0 = 1$ |
| 3 | 11 | 1 | 1 | 1 | $1 + 1 = 2$ |
| 4 | 100 | 2 | 1 | 0 | $1 + 0 = 1$ |
| 5 | 101 | 2 | 1 | 1 | $1 + 1 = 2$ |

**2.4 Pattern Explanation:**

- For even numbers: `countBits(i) = countBits(i//2)` (right shift removes trailing 0)
- For odd numbers: `countBits(i) = countBits(i//2) + 1` (right shift removes the trailing 1, which we add back)

**2.5 Return Result:**

We return `[0, 1, 1, 2, 1, 2]`, which represents the number of 1's in binary for 0 through 5.

> **Note:** The key insight is that removing the least significant bit (via right shift) gives us a smaller number whose bit count we've already computed. We just need to add back the removed bit if it was 1.

