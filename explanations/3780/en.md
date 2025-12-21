## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an integer array. We need to choose exactly three integers such that their sum is divisible by 3, and return the maximum possible sum. If no such triplet exists, return 0.

**1.1 Constraints & Complexity:**

- **Input Size:** Up to 10^5 elements in the array.
- **Time Complexity:** O(n log n) where n is the length of nums - we need to sort the numbers by remainder groups, which takes O(n log n).
- **Space Complexity:** O(n) to store the three remainder groups.
- **Edge Case:** If there are fewer than 3 numbers, or no valid combination exists, we return 0.

**1.2 High-level approach:**

The goal is to group numbers by their remainder when divided by 3 (0, 1, or 2), then find the maximum sum from valid combinations: three 0s, three 1s, three 2s, or one from each group.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible triplets, check if sum is divisible by 3, and track the maximum. This would be O(n^3) which is too slow for large inputs.
- **Optimized Strategy:** Group by remainder, sort each group in descending order, then check the four valid combinations. This is O(n log n) time.
- **Optimization:** By grouping by remainder, we reduce the problem to checking only 4 specific combinations instead of all possible triplets, making it much more efficient.

**1.4 Decomposition:**

1. Group numbers by their remainder when divided by 3 (remainder 0, 1, or 2).
2. Sort each group in descending order.
3. Check four valid combinations:
   - Three numbers with remainder 0.
   - Three numbers with remainder 1.
   - Three numbers with remainder 2.
   - One number from each remainder group (0, 1, 2).
4. Return the maximum sum from these valid combinations.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [4, 2, 3, 1]`

- Group by remainder:
  - Remainder 0: `[3]` (3 % 3 = 0)
  - Remainder 1: `[4, 1]` (4 % 3 = 1, 1 % 3 = 1)
  - Remainder 2: `[2]` (2 % 3 = 2)
- After sorting descending: `rem[0] = [3]`, `rem[1] = [4, 1]`, `rem[2] = [2]`

**2.2 Start Checking:**

We check each of the four valid combinations to find the maximum sum.

**2.3 Trace Walkthrough:**

| Combination | Numbers | Sum | Valid? | Result |
| ----------- | ------- | --- | ------ | ------ |
| Three 0s | Need 3, have 1 | - | No | - |
| Three 1s | Need 3, have 2 | - | No | - |
| Three 2s | Need 3, have 1 | - | No | - |
| One from each | 3, 4, 2 | 3 + 4 + 2 = 9 | Yes | 9 |

The only valid combination is one from each remainder group: 3 (rem 0) + 4 (rem 1) + 2 (rem 2) = 9, which is divisible by 3.

**2.4 Increment and Loop:**

We check all four combinations and track the maximum valid sum.

**2.5 Return Result:**

The result is 9, which is the maximum sum of three numbers (3, 4, 2) whose sum is divisible by 3.

