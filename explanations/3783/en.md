## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an integer, we need to calculate the sum of absolute differences between corresponding digits from the left and right ends (mirror distance).

**1.1 Constraints & Complexity:**

- **Input Size:** The integer can be up to 10^9.
- **Time Complexity:** O(log n) - we need to process each digit pair, where the number of digits is O(log n).
- **Space Complexity:** O(log n) - we need to convert the number to a string to access digits.
- **Edge Case:** If the number has only one digit, return 0. If the number has an odd number of digits, the middle digit is not paired.

**1.2 High-level approach:**

The goal is to pair digits from both ends (first with last, second with second-to-last, etc.) and sum the absolute differences.

![Mirror distance visualization](https://assets.leetcode.com/static_assets/others/mirror-distance.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** This problem is straightforward - we just need to pair digits and calculate differences. The approach is already optimal.
- **Optimized Strategy:** Convert to string, iterate through half the digits, and pair with corresponding digits from the end. This is O(log n) time.
- **Optimization:** By processing only half the digits and using string indexing, we solve efficiently.

**1.4 Decomposition:**

1. Convert the integer to a string to access individual digits.
2. For each position from 0 to n/2 - 1:
   - Get the digit at position i.
   - Get the digit at position n-1-i (mirror position).
   - Calculate absolute difference.
   - Add to result.
3. Return the total sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `num = 1234`

- String: `"1234"`
- Length: `4`
- Result variable: `res = 0`

**2.2 Start Checking:**

We pair digits from both ends.

**2.3 Trace Walkthrough:**

| Step | i | Left digit | Right digit | Difference | res |
| ---- | - | ---------- | ----------- | ---------- | --- |
| 1    | 0 | '1' (1) | '4' (4) | |1-4| = 3 | 3 |
| 2    | 1 | '2' (2) | '3' (3) | |2-3| = 1 | 4 |

**2.4 Increment and Loop:**

After processing each pair, we move to the next pair.

**2.5 Return Result:**

The result is `4`, which is the sum of absolute differences: |1-4| + |2-3| = 3 + 1 = 4.
