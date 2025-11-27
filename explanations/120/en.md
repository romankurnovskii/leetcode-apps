## Explanation

### Strategy (The "Why")

Given a triangle array, we need to find the minimum path sum from top to bottom. At each step, you may move to an adjacent number in the row below.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of rows $n$ can be between $1$ and $200$.
- **Value Range:** Each element is between $-10^4$ and $10^4$.
- **Time Complexity:** $O(n^2)$ - We visit each element in the triangle once.
- **Space Complexity:** $O(1)$ - We modify the input triangle in-place, using only constant extra space.
- **Edge Case:** If the triangle has only one row, return that single element.

**1.2 High-level approach:**

The goal is to find the minimum path sum from top to bottom of a triangle.

![Triangle](https://assets.leetcode.com/uploads/2020/11/14/triangle.jpg)

We use dynamic programming bottom-up. Starting from the second-to-last row, we update each element to be the sum of itself plus the minimum of its two children below.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths from top to bottom, calculating the sum for each. This would be exponential time.
- **Optimized Strategy (DP Bottom-up):** Work from bottom to top, storing the minimum path sum to reach each position. This takes $O(n^2)$ time.
- **Why it's better:** DP reduces the time complexity from exponential to polynomial. By working bottom-up, we ensure each subproblem is solved only once.

**1.4 Decomposition:**

1. Start from the second-to-last row.
2. For each element in the current row, add the minimum of its two children below.
3. Continue upward until reaching the top.
4. Return the top element, which now contains the minimum path sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]$

**2.2 Start Processing:**

We begin from row 2 (second-to-last).

**2.3 Trace Walkthrough:**

| Row | Before | After | Explanation |
|-----|--------|-------|-------------|
| 3 | $[4,1,8,3]$ | $[4,1,8,3]$ | Last row, no change |
| 2 | $[6,5,7]$ | $[7,6,10]$ | $6+\min(4,1)=7$, $5+\min(1,8)=6$, $7+\min(8,3)=10$ |
| 1 | $[3,4]$ | $[9,10]$ | $3+\min(7,6)=9$, $4+\min(6,10)=10$ |
| 0 | $[2]$ | $[11]$ | $2+\min(9,10)=11$ |

**2.4 Final Result:**

The top element becomes 11, which is the minimum path sum.

**2.5 Return Result:**

We return 11, which represents the minimum path: $2 \rightarrow 3 \rightarrow 5 \rightarrow 1 = 11$.

> **Note:** Working bottom-up ensures that when we process a row, all rows below it already contain the minimum path sums to the bottom. This creates optimal substructure.

