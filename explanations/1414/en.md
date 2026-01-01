## Explanation

### Strategy (The "Why")

**Restate the problem:** Given an integer k, we need to find the minimum number of Fibonacci numbers (each used at most once) whose sum equals k.

**1.1 Constraints & Complexity:**

- **Input Size:** k can be up to 10^9.
- **Time Complexity:** O(log k) - we generate Fibonacci numbers up to k (which takes O(log k) since Fibonacci grows exponentially), then use a greedy approach.
- **Space Complexity:** O(log k) - we need to store Fibonacci numbers up to k, which is O(log k) in count.
- **Edge Case:** If k is a Fibonacci number itself, the answer is 1. If k is 0, the answer is 0 (though k >= 1 by constraints).

**1.2 High-level approach:**

The goal is to use a greedy approach: repeatedly subtract the largest Fibonacci number that is less than or equal to the remaining value until we reach 0. This works because of the mathematical property of Fibonacci numbers.

![Fibonacci sum visualization](https://assets.leetcode.com/static_assets/others/fibonacci-sum.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible combinations of Fibonacci numbers to sum to k. This is exponential.
- **Optimized Strategy:** Use a greedy approach - always subtract the largest possible Fibonacci number. This is O(log k) time.
- **Optimization:** The greedy approach works because of the mathematical property that any positive integer can be represented as a sum of distinct Fibonacci numbers (Zeckendorf's theorem), and the greedy choice is optimal.

**1.4 Decomposition:**

1. Generate Fibonacci numbers up to k.
2. Start from the largest Fibonacci number and work backwards.
3. For each Fibonacci number, if it's less than or equal to the remaining k, subtract it and increment the count.
4. Continue until k becomes 0.
5. Return the count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `k = 7`

- Fibonacci numbers up to 7: `[1, 1, 2, 3, 5]` (we'll use [1, 2, 3, 5] excluding duplicates)
- Remaining value: `k = 7`
- Count: `res = 0`

**2.2 Start Checking:**

We begin subtracting Fibonacci numbers from largest to smallest.

**2.3 Trace Walkthrough:**

| Step | Largest Fib <= k | Subtract | k after | res |
| ---- | ---------------- | -------- | ------- | --- |
| 1    | 5                | 5        | 2       | 1   |
| 2    | 2                | 2        | 0       | 2   |

**2.4 Increment and Loop:**

After each subtraction, we check if k > 0. If yes, we continue with the next largest Fibonacci number.

**2.5 Return Result:**

The result is `2`, which means we need 2 Fibonacci numbers (5 and 2) to sum to 7.

