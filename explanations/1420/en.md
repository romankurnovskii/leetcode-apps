## Explanation

### Strategy (The "Why")

**Restate the problem:** Given integers n, m, and k, we need to count the number of ways to build an array of length n where each element is between 1 and m, and the maximum element is found exactly k times when searching through the array.

**1.1 Constraints & Complexity:**

- **Input Size:** n and m can be up to 50, and k can be up to n.
- **Time Complexity:** O(n * m * k) - we use dynamic programming with three dimensions: array length, maximum value, and number of comparisons.
- **Space Complexity:** O(n * m * k) - we need a 3D DP array, but we can optimize to O(m * k) by only keeping the previous state.
- **Edge Case:** If k > n, return 0 (impossible). If k = 0 and n > 0, return 0 (we must find the maximum at least once if array is non-empty).

**1.2 High-level approach:**

The goal is to use dynamic programming where we track: for arrays of length i, with maximum value j, and exactly l comparisons made. We can optimize space by only keeping the previous row's state.

![Array building visualization](https://assets.leetcode.com/static_assets/others/array-build.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible arrays and count how many times the maximum is found. This is exponential (m^n).
- **Optimized Strategy:** Use dynamic programming to count valid arrays by tracking maximum value and comparison count. This is O(n * m * k) time.
- **Optimization:** By using DP and tracking only the necessary state (maximum value and comparison count), we avoid generating all possible arrays.

**1.4 Decomposition:**

1. Initialize DP where dp[i][j][l] = number of arrays of length i, max value j, with l comparisons.
2. For each array length from 1 to n:
   - For each possible maximum value from 1 to m:
     - For each comparison count from 0 to k:
       - If we add a number <= current max: no new comparison (add to same state).
       - If we add a number > current max: new comparison (add to new max state with l+1 comparisons).
3. Sum all dp[n][j][k] for j from 1 to m.
4. Return the result modulo 10^9 + 7.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 2`, `m = 3`, `k = 1`

- DP state: `dp[i][max_val][comparisons]`
- Base case: `dp[0][0][0] = 1`
- Result variable: `res = 0`

**2.2 Start Checking:**

We begin building arrays of increasing length.

**2.3 Trace Walkthrough:**

| Step | i | j | l | Add num <= j | Add num > j | dp[i][j][l] |
| ---- | - | - | - | ------------ | ----------- | ----------- |
| 1    | 1 | 1 | 0 | 1 way (add 1) | - | 1 |
| 2    | 1 | 2 | 0 | 1 way (add 2) | 1 way (add 2, l=1) | 1 (l=0), 1 (l=1) |
| 3    | 1 | 3 | 0 | 1 way (add 3) | 1 way (add 3, l=1) | 1 (l=0), 1 (l=1) |
| 4    | 2 | 1 | 1 | From dp[1][1][0]: add 1 | - | ... |
| ...  | ... | ... | ... | ... | ... | ... |

**2.4 Increment and Loop:**

After processing each length, we move to the next length and continue.

**2.5 Return Result:**

The result is the sum of all ways to build arrays of length n with exactly k comparisons, which we calculate by summing dp[n][j][k] for all j from 1 to m.

