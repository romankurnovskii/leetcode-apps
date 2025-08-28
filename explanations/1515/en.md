## 1515. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K [Medium]

https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k

## Description
Given an integer `k`, *return the minimum number of Fibonacci numbers whose sum is equal to* `k`. The same Fibonacci number can be used multiple times.

The Fibonacci numbers are defined as:

- `F₁ = 1`
- `F₂ = 1`
- `Fₙ = Fₙ₋₁ + Fₙ₋₂` for `n > 2`

It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to `k`.

**Examples**

```tex
Example 1:
Input: k = 7
Output: 2
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
For k = 7 we can use 2 + 5 = 7.

Example 2:
Input: k = 10
Output: 2
Explanation: For k = 10 we can use 2 + 8 = 10.

Example 3:
Input: k = 19
Output: 3
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
```

**Constraints**
```tex
- 1 <= k <= 10^9
```

## Explanation

### Strategy
Let's restate the problem: You're given a target integer `k`, and you need to find the minimum number of Fibonacci numbers that sum to `k`. You can use the same Fibonacci number multiple times, and it's guaranteed that a solution exists.

This is a **greedy problem** that can be solved by always choosing the largest possible Fibonacci number that doesn't exceed the remaining sum.

**What is given?** A target integer `k` that can be very large (up to 10⁹).

**What is being asked?** Find the minimum number of Fibonacci numbers that sum to `k`.

**Constraints:** The target `k` can be up to 10⁹, which means we need an efficient approach.

**Edge cases:** 
- `k = 1` (single Fibonacci number)
- `k` is itself a Fibonacci number
- `k` requires multiple Fibonacci numbers

**High-level approach:**
The solution involves generating Fibonacci numbers up to `k`, then using a greedy approach to always select the largest possible Fibonacci number that fits in the remaining sum.

**Decomposition:**
1. **Generate Fibonacci numbers**: Create all Fibonacci numbers up to `k`
2. **Greedy selection**: Always choose the largest Fibonacci number that fits
3. **Subtract and repeat**: Subtract the chosen number and continue until sum reaches 0
4. **Count operations**: Track how many Fibonacci numbers were used

**Brute force vs. optimized strategy:**
- **Brute force**: Try all combinations of Fibonacci numbers. This is extremely inefficient.
- **Optimized**: Use greedy approach with pre-generated Fibonacci numbers. This takes O(log k) time.

### Steps
Let's walk through the solution step by step using the first example: `k = 7`

**Step 1: Generate Fibonacci numbers up to k**
- Start with F₁ = 1, F₂ = 1
- F₃ = F₂ + F₁ = 1 + 1 = 2
- F₄ = F₃ + F₂ = 2 + 1 = 3
- F₅ = F₄ + F₃ = 3 + 2 = 5
- F₆ = F₅ + F₄ = 5 + 3 = 8 (exceeds 7, stop)
- Fibonacci numbers up to 7: [1, 1, 2, 3, 5]

**Step 2: Greedy selection process**
- **Remaining sum**: 7
- **Largest Fibonacci ≤ 7**: 5
- **Use 5**: 7 - 5 = 2
- **Count**: 1

- **Remaining sum**: 2
- **Largest Fibonacci ≤ 2**: 2
- **Use 2**: 2 - 2 = 0
- **Count**: 2

- **Remaining sum**: 0
- **Process complete**

**Step 3: Result**
- Total Fibonacci numbers used: 2
- Solution: 5 + 2 = 7

**Why this works:**
The greedy approach works because:
1. **Optimal substructure**: If we can represent `k` with `n` Fibonacci numbers, then representing `k - F_max` with `n-1` numbers must also be optimal
2. **Greedy choice property**: Always choosing the largest possible Fibonacci number ensures we use the minimum number of terms
3. **Fibonacci properties**: Each Fibonacci number is the sum of the two preceding ones, making the greedy choice optimal

> **Note:** The key insight is that using the largest possible Fibonacci number at each step minimizes the total count. This works because Fibonacci numbers have the property that no smaller combination can sum to a larger value more efficiently.

**Time Complexity:** O(log k) - we generate Fibonacci numbers up to k, which grows exponentially  
**Space Complexity:** O(log k) - we store the generated Fibonacci numbers
