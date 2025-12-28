## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to construct an array of n distinct positive integers from 1 to n such that the absolute differences between adjacent elements have exactly k distinct values. If multiple valid answers exist, we can return any of them.

**1.1 Constraints & Complexity:**

- **Input Size:** n is between 2 and 10^4, and k is between 1 and n-1.
- **Time Complexity:** O(n) - we iterate through n elements once, building the result array.
- **Space Complexity:** O(n) - we store the result array of size n.
- **Edge Case:** When k = 1, we can return [1, 2, 3, ..., n] or [n, n-1, ..., 1] since all differences are 1.

**1.2 High-level approach:**

The goal is to create k distinct differences by interleaving numbers from the start and end of the range. For the first k-1 positions, we alternate between taking the smallest available number and the largest available number. After that, we fill the rest with consecutive numbers, which all have difference 1.

![Interleaving pattern visualization](https://assets.leetcode.com/static_assets/others/interleaving-pattern.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all permutations of [1, 2, ..., n] and check which ones have k distinct differences. This requires O(n! × n) time, which is infeasible.
- **Optimized Strategy:** Use a greedy construction approach. Interleave numbers from both ends for the first k-1 elements to create k distinct differences, then fill the rest with consecutive numbers. This is O(n) time.
- **Optimization:** By recognizing the pattern that interleaving creates distinct differences, we can construct the answer directly without trying all possibilities, reducing complexity from O(n!) to O(n).

**1.4 Decomposition:**

1. Initialize two pointers: `left = 1` (start of range) and `right = n` (end of range).
2. For the first k-1 elements, alternate between taking from `left` and `right`:
   - If k is odd, take from `left` and increment it.
   - If k is even, take from `right` and decrement it.
   - Decrement k after each step.
3. After creating k-1 distinct differences, fill the remaining positions with consecutive numbers from `left`.
4. Return the constructed array.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 3, k = 2`

- Range: [1, 2, 3]
- Initialize: `left = 1`, `right = 3`

**2.2 Start Checking:**

We begin constructing the array by alternating between left and right.

**2.3 Trace Walkthrough:**

| Step | k   | k % 2 | Action        | res      | left | right | Differences (so far) |
| ---- | --- | ----- | ------------- | -------- | ---- | ----- | -------------------- |
| 0    | 2   | 0     | Take right=3  | [3]      | 1    | 2     | -                    |
| 1    | 1   | 1     | Take left=1    | [3,1]    | 2    | 2     | [2]                  |
| 2    | 1   | -     | Take left=2    | [3,1,2]  | 3    | 2     | [2, 1]               |

Final differences: |3-1| = 2, |1-2| = 1. Distinct differences: {1, 2} = 2 distinct values ✓

**2.4 Increment and Loop:**

For each position:
- If k > 1, we alternate between taking from left and right to create distinct differences.
- We decrement k after each alternation.
- Once k reaches 1, we fill the rest with consecutive numbers from left.

**2.5 Return Result:**

The result is [3, 1, 2], which has exactly 2 distinct differences: 2 and 1.

