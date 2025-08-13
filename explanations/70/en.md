# 70. Climbing Stairs [Easy]

## Problem Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**
```text
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:**
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:**
- `1 <= n <= 45`

## Explanation

### Strategy

This is a **dynamic programming problem** that follows the Fibonacci sequence pattern. The key insight is that the number of ways to reach step n is the sum of ways to reach step (n-1) and step (n-2).

**Key observations:**
- To reach step n, you can come from step (n-1) by taking 1 step
- Or you can come from step (n-2) by taking 2 steps
- The total ways = ways to reach (n-1) + ways to reach (n-2)
- This forms the Fibonacci sequence: F(n) = F(n-1) + F(n-2)

**High-level approach:**
1. **Base cases**: F(1) = 1, F(2) = 2
2. **Recursive formula**: F(n) = F(n-1) + F(n-2)
3. **Iterative solution**: Use two variables to track previous values
4. **Space optimization**: Only need to keep track of last two values

### Steps

Let's break down the solution step by step:

**Step 1: Handle base cases**
- If n = 1, return 1
- If n = 2, return 2

**Step 2: Initialize variables**
- `prev = 1`: Ways to reach step 1
- `curr = 2`: Ways to reach step 2

**Step 3: Iterate from 3 to n**
- For each step i from 3 to n:
  - Calculate next value: `next = prev + curr`
  - Update variables: `prev = curr, curr = next`

**Step 4: Return result**
- Return `curr` (ways to reach step n)

**Example walkthrough:**
Let's trace through the second example:

```text
n = 3

Step 1: Initialize
prev = 1, curr = 2

Step 2: Calculate for step 3
next = prev + curr = 1 + 2 = 3
prev = 2, curr = 3

Step 3: Return result
curr = 3

Result: 3
```

> **Note:** The key insight is that this problem follows the Fibonacci sequence. The number of ways to reach step n is the sum of ways to reach the previous two steps, which creates an optimal substructure perfect for dynamic programming.

**Time Complexity:** O(n) - we iterate from 3 to n  
**Space Complexity:** O(1) - we only use a constant amount of extra space 