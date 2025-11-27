## Explanation

### Strategy (The "Why")

Given an array `cost` where `cost[i]` is the cost of stepping on the $i$-th step, we need to find the minimum cost to reach the top of the floor. We can start from step 0 or step 1, and can climb either 1 or 2 steps at a time.

**1.1 Constraints & Complexity:**

- **Input Size:** The array length $N$ can be between $2$ and $1000$.
- **Value Range:** Each cost value is between $0$ and $999$.
- **Time Complexity:** $O(n)$ - We iterate through the cost array once, computing the minimum cost for each step.
- **Space Complexity:** $O(n)$ - We use a DP array of size $n+1$ to store the minimum cost to reach each step. This can be optimized to $O(1)$ by using only two variables.
- **Edge Case:** We can start at step 0 or step 1 with cost 0. The top of the floor is at index $n$ (one step beyond the last step in the array).

**1.2 High-level approach:**

The goal is to find the minimum cost to reach the top of the floor.

![Climbing Stairs](https://assets.leetcode.com/uploads/2020/10/25/cost-easy-1.png)

This is a classic dynamic programming problem. At each step, we can arrive from either the previous step or two steps back. We choose the path with minimum cost.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths from step 0 or step 1 to the top, calculating the cost for each path. This would be exponential time $O(2^n)$.
- **Optimized Strategy (Dynamic Programming):** Use DP to store the minimum cost to reach each step. For step $i$, the minimum cost is the minimum of: (cost to reach step $i-1$ + cost of step $i-1$) or (cost to reach step $i-2$ + cost of step $i-2$).
- **Why it's better:** DP reduces the time complexity from exponential to linear. We compute each subproblem once and reuse the results, avoiding redundant calculations.

**1.4 Decomposition:**

1. Initialize a DP array where `dp[i]` represents the minimum cost to reach step $i$.
2. Set base cases: `dp[0] = 0` and `dp[1] = 0` (we can start at either step for free).
3. For each step from 2 to $n$:
   - Calculate the cost of reaching from step $i-1$: `dp[i-1] + cost[i-1]`
   - Calculate the cost of reaching from step $i-2$: `dp[i-2] + cost[i-2]`
   - Take the minimum of these two options.
4. Return `dp[n]`, which is the minimum cost to reach the top.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $cost = [10, 15, 20]$

We initialize:
- `dp = [0, 0]` (cost to reach step 0 and step 1 is 0)
- We need to reach step 3 (the top, which is one step beyond the last step)

**2.2 Start Calculating:**

We begin calculating from step 2.

**2.3 Trace Walkthrough:**

| Step | Cost Array | dp[i-1] + cost[i-1] | dp[i-2] + cost[i-2] | dp[i] = min(...) |
|------|------------|---------------------|---------------------|------------------|
| 0 | [10, 15, 20] | - | - | 0 (base case) |
| 1 | [10, 15, 20] | - | - | 0 (base case) |
| 2 | [10, 15, 20] | $0 + 15 = 15$ | $0 + 10 = 10$ | $\min(15, 10) = 10$ |
| 3 | [10, 15, 20] | $10 + 20 = 30$ | $0 + 15 = 15$ | $\min(30, 15) = 15$ |

Detailed calculation:
- **Step 2:** We can reach from step 1 (cost: $0 + 15 = 15$) or step 0 (cost: $0 + 10 = 10$). Minimum is 10.
- **Step 3 (top):** We can reach from step 2 (cost: $10 + 20 = 30$) or step 1 (cost: $0 + 15 = 15$). Minimum is 15.

**2.4 Path Visualization:**

The optimal path: Start at step 1 (cost 0) → Step 3 (pay cost 15 from step 1) = Total cost 15.

**2.5 Return Result:**

We return `dp[3] = 15`, which is the minimum cost to reach the top.

> **Note:** The key insight is that we pay the cost when leaving a step, not when arriving at it. So to reach step $i$ from step $i-1$, we pay `cost[i-1]`.

