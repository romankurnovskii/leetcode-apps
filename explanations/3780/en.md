## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an array of integers, we need to find the maximum sum of three numbers that is divisible by 3.

**1.1 Constraints & Complexity:**

- **Input Size:** The array can have up to 10^4 elements.
- **Time Complexity:** O(n log n) - we need to sort the numbers in each modulo group, where n is the array length.
- **Space Complexity:** O(n) - we need to store numbers in three groups based on their modulo 3 value.
- **Edge Case:** If there are fewer than 3 numbers, return -1. If no combination sums to a multiple of 3, return -1.

**1.2 High-level approach:**

The goal is to group numbers by their remainder when divided by 3, then find the maximum sum of three numbers that is divisible by 3. This can be achieved by either taking three numbers from the same group (all mod 0, all mod 1, or all mod 2) or one from each group.

![Modulo grouping visualization](https://assets.leetcode.com/static_assets/others/modulo-group.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all combinations of three numbers. This is O(n^3) which is inefficient.
- **Optimized Strategy:** Group by modulo 3, sort each group, and check the maximum sum from valid combinations. This is O(n log n) time.
- **Optimization:** By using the mathematical property that (a+b+c) mod 3 = (a mod 3 + b mod 3 + c mod 3) mod 3, we can efficiently find valid combinations.

**1.4 Decomposition:**

1. Group numbers by their remainder when divided by 3 (mod 0, mod 1, mod 2).
2. Sort each group in descending order.
3. Check four cases:
   - Three numbers from mod 0 group.
   - Three numbers from mod 1 group.
   - Three numbers from mod 2 group.
   - One number from each group.
4. Return the maximum sum among valid cases, or -1 if none exists.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [3, 6, 5, 1, 8]`

- Mod 0: `[3, 6]` → sorted: `[6, 3]`
- Mod 1: `[1]` → sorted: `[1]`
- Mod 2: `[5, 8]` → sorted: `[8, 5]`
- Result variable: `res = -1`

**2.2 Start Checking:**

We check all valid combinations.

**2.3 Trace Walkthrough:**

| Step | Combination | Sum | Valid? | res |
| ---- | ----------- | --- | ------ | --- |
| 1    | 6+3+6 (mod0) | 15 | No (only 2 in mod0) | -1 |
| 2    | 1+1+1 (mod1) | 3 | No (only 1 in mod1) | -1 |
| 3    | 8+5+8 (mod2) | 21 | No (only 2 in mod2) | -1 |
| 4    | 6+1+8 (one each) | 15 | Yes (15%3=0) | 15 |

**2.4 Increment and Loop:**

We check each combination and update the maximum.

**2.5 Return Result:**

The result is `15`, which is the maximum sum of three numbers (6, 1, 8) that is divisible by 3.
