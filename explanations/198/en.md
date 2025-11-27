## Explanation

### Strategy (The "Why")

Given an array `nums` representing the amount of money in each house, we need to determine the maximum amount of money we can rob tonight without alerting the police. The constraint is that we cannot rob two adjacent houses.

**1.1 Constraints & Complexity:**

- **Input Size:** The number of houses $N$ can be between $1$ and $100$.
- **Value Range:** Each house contains between $0$ and $400$ dollars.
- **Time Complexity:** $O(n)$ - We iterate through the array once, computing the maximum money for each position.
- **Space Complexity:** $O(n)$ - We use a DP array of size $n$ to store the maximum money robbed up to each house. This can be optimized to $O(1)$ by using only two variables.
- **Edge Case:** If there's only one house, we rob it. If there are two houses, we rob the one with more money.

**1.2 High-level approach:**

The goal is to maximize the total money robbed without robbing two adjacent houses.

![House Robber](https://assets.leetcode.com/uploads/2021/04/19/rob1-tree.jpg)

This is a classic dynamic programming problem. At each house, we decide whether to rob it (and skip the previous house) or skip it (and keep the maximum from previous houses).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of houses to rob, checking that no two are adjacent. This would be exponential time $O(2^n)$.
- **Optimized Strategy (Dynamic Programming):** Use DP to store the maximum money we can rob up to each house. For house $i$, we either rob it (taking `dp[i-2] + nums[i]`) or skip it (taking `dp[i-1]`).
- **Why it's better:** DP reduces the time complexity from exponential to linear. We compute each subproblem once, avoiding redundant calculations of overlapping subproblems.

**1.4 Decomposition:**

1. Handle base cases: if $n = 0$, return 0; if $n = 1$, return `nums[0]`; if $n = 2$, return `max(nums[0], nums[1])`.
2. Initialize a DP array where `dp[i]` represents the maximum money robbed up to house $i$.
3. Set `dp[0] = nums[0]` and `dp[1] = max(nums[0], nums[1])`.
4. For each house from index 2 to $n-1$:
   - Calculate the maximum of: robbing current house (`dp[i-2] + nums[i]`) or skipping it (`dp[i-1]`).
5. Return `dp[n-1]`, which is the maximum money we can rob.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $nums = [2, 7, 9, 3, 1]$

We initialize:
- `dp[0] = 2` (rob first house)
- `dp[1] = max(2, 7) = 7` (rob second house, skip first)

**2.2 Start Calculating:**

We begin calculating from index 2.

**2.3 Trace Walkthrough:**

| Index | House Value | dp[i-2] + nums[i] | dp[i-1] | dp[i] = max(...) | Decision |
|-------|-------------|-------------------|---------|------------------|----------|
| 0 | 2 | - | - | 2 | Rob house 0 |
| 1 | 7 | - | - | 7 | Rob house 1 |
| 2 | 9 | $2 + 9 = 11$ | $7$ | $\max(11, 7) = 11$ | Rob house 2 |
| 3 | 3 | $7 + 3 = 10$ | $11$ | $\max(10, 11) = 11$ | Skip house 3 |
| 4 | 1 | $11 + 1 = 12$ | $11$ | $\max(12, 11) = 12$ | Rob house 4 |

Detailed calculation:
- **Index 2:** Rob house 2 ($2 + 9 = 11$) or keep previous max ($7$). Choose 11.
- **Index 3:** Rob house 3 ($7 + 3 = 10$) or keep previous max ($11$). Choose 11 (skip house 3).
- **Index 4:** Rob house 4 ($11 + 1 = 12$) or keep previous max ($11$). Choose 12.

**2.4 Optimal Path:**

The optimal path: Rob houses at indices 0, 2, and 4: $2 + 9 + 1 = 12$.

**2.5 Return Result:**

We return `dp[4] = 12`, which is the maximum money we can rob.

> **Note:** The key insight is that at each house, we have two choices: rob it (and take the best from two houses ago) or skip it (and keep the best from the previous house). We always choose the option that maximizes our total.

