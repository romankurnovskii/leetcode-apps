## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= n, m <= 1000`.
- **Time Complexity:** O(n) - we iterate through numbers from 1 to n once.
- **Space Complexity:** O(1) - we only use constant space for the sum variables.
- **Edge Case:** When `m > n`, no numbers are divisible by m, so num2 = 0.

**1.2 High-level approach:**
The goal is to calculate the difference between the sum of numbers not divisible by `m` and the sum of numbers divisible by `m` in the range [1, n]. We iterate through all numbers and categorize them.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we need to check each number once.
- **Optimized Strategy:** Single pass through numbers 1 to n, checking divisibility and accumulating sums.

**1.4 Decomposition:**
1. Initialize two sum variables: one for divisible numbers, one for non-divisible numbers.
2. Iterate through numbers from 1 to n.
3. Check if each number is divisible by m.
4. Add to the appropriate sum variable.
5. Return the difference.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `n = 10, m = 3`. We initialize `num1 = 0` (non-divisible sum) and `num2 = 0` (divisible sum).

**2.2 Start Checking:**
We iterate through numbers from 1 to 10.

**2.3 Trace Walkthrough:**

| i | i % 3 | Divisible? | num1 | num2 |
|---|-------|------------|------|------|
| 1 | 1 | No | 1 | 0 |
| 2 | 2 | No | 3 | 0 |
| 3 | 0 | Yes | 3 | 3 |
| 4 | 1 | No | 7 | 3 |
| 5 | 2 | No | 12 | 3 |
| 6 | 0 | Yes | 12 | 9 |
| 7 | 1 | No | 19 | 9 |
| 8 | 2 | No | 27 | 9 |
| 9 | 0 | Yes | 27 | 18 |
| 10 | 1 | No | 37 | 18 |

**2.4 Increment and Loop:**
After processing each number, we increment and continue until we reach n.

**2.5 Return Result:**
Return `res = num1 - num2 = 37 - 18 = 19`.

