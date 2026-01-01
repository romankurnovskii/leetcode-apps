## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an integer n, we need to count the number of ways to paint an n × 3 grid using three colors such that no two adjacent cells (horizontally or vertically) have the same color.

**1.1 Constraints & Complexity:**

- **Input Size:** n can be up to 5000.
- **Time Complexity:** O(n) - we iterate through n rows, and for each row we calculate the number of valid colorings based on the previous row in constant time.
- **Space Complexity:** O(1) - we only need to track two states (ABA and ABC patterns) regardless of n.
- **Edge Case:** If n = 1, we can paint the row in 3 * 2 = 6 ways (3 choices for first cell, 2 for second, 2 for third, but with constraints).

**1.2 High-level approach:**

The goal is to use dynamic programming to track two types of row patterns: ABA (where first and third cells have the same color) and ABC (where all three cells have different colors). Each row's valid colorings depend on the previous row's pattern.

![Grid painting visualization](https://assets.leetcode.com/static_assets/others/grid-painting.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible colorings of the entire grid and count valid ones. This is exponential (3^(3n)) and completely impractical.
- **Optimized Strategy:** Use DP to track only the two possible row patterns (ABA and ABC) and calculate transitions between them. This is O(n) time.
- **Optimization:** By recognizing that only two row patterns matter and tracking transitions between them, we reduce the state space from exponential to linear.

**1.4 Decomposition:**

1. Initialize counts for ABA and ABC patterns for the first row.
2. For each subsequent row, calculate new counts based on valid transitions from previous row patterns.
3. A row with pattern ABA can transition to ABC patterns in 2 ways.
4. A row with pattern ABC can transition to both ABA (2 ways) and ABC (2 ways) patterns.
5. Sum the final counts and return modulo 10^9 + 7.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 2`

- First row: `aba = 6` (ABA patterns), `abc = 6` (ABC patterns)
- Result variable: `res = 0`

**2.2 Start Checking:**

We begin calculating transitions for the second row.

**2.3 Trace Walkthrough:**

| Step | Row | aba | abc | Calculation |
| ---- | --- | --- | --- | ----------- |
| 1    | 1   | 6   | 6   | Initial state |
| 2    | 2   | 30  | 24  | aba = 6*3 + 6*2 = 30, abc = 6*2 + 6*2 = 24 |
| 3    | -   | -   | -   | Total = 30 + 24 = 54 |

**2.4 Increment and Loop:**

After processing each row, we update the counts and move to the next row.

**2.5 Return Result:**

The result is `54`, which is the number of ways to paint a 2 × 3 grid with the given constraints.

